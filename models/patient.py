from odoo import models, fields, api, _


class DoctorAppointment(models.Model):
    _name = 'doctor.appointment'
    _description = 'Doctor Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Appointment Title', required=True)
    appointment_date = fields.Datetime('Appointment Date', required=True)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending', string='Status', track_visibility='onchange')

    patient_name = fields.Char(string='Patient', required=True)
    doctor_id = fields.Many2one('hr.employee', string='Doctor', required=True)
    appointment_type = fields.Selection([
        ('in_person', 'In-person'),
        ('virtual', 'Virtual')
    ], default='in_person', string='Appointment Type')

    medical_history = fields.Text('Medical History')
    reason_for_visit = fields.Text('Reason for Visit')

    start_time = fields.Datetime('Start Time', required=True)
    end_time = fields.Datetime('End Time', required=False)

    # রেকর্ড তৈরি করার সময় সিঙ্ক্রোনাইজ লজিক
    @api.model_create_multi
    def create(self, vals_list):
        # ডিফল্ট create মেথড কল করা
        records = super(DoctorAppointment, self).create(vals_list)

        # প্রতিটি নতুন রেকর্ডের জন্য schedule রেকর্ড তৈরি করা
        for record in records:
            self.env['appointment.schedule'].create({
                'appointment_id': record.id,
                'name': record.name,
                'appointment_date': record.appointment_date,
                'state': record.state,
                'patient_name': record.patient_name,
                'doctor_id': record.doctor_id.id,
                'appointment_type': record.appointment_type,
            })
        return records

    # রেকর্ড আপডেট করার সময় সিঙ্ক্রোনাইজ লজিক
    def write(self, vals):
        res = super(DoctorAppointment, self).write(vals)

        # প্রতিটি আপডেট হওয়া রেকর্ডের schedule রেকর্ড আপডেট করা
        for record in self:
            schedule = self.env['appointment.schedule'].search([('appointment_id', '=', record.id)], limit=1)
            if schedule:
                schedule.write({
                    'name': record.name,
                    'appointment_date': record.appointment_date,
                    'state': record.state,
                    'patient_name': record.patient_name,
                    'doctor_id': record.doctor_id.id,
                    'appointment_type': record.appointment_type,
                })
        return res

    def action_pending(self):
        self.state = 'pending'

    def action_confirm(self):
        self.state = 'confirmed'

    def action_completed(self):
        self.state = 'completed'

    def action_cancel(self):
        self.state = 'cancel'