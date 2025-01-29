from odoo import models, fields, _


class AppointmentSchedule(models.Model):
    _name = 'appointment.schedule'
    _description = 'Appointment Schedule'

    appointment_id = fields.Many2one('doctor.appointment', string='Appointment', required=True, ondelete='cascade')
    name = fields.Char(string='Appointment Title', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', required=True)
    patient_name = fields.Char(string='Patient', required=True)
    doctor_id = fields.Many2one('hr.employee', string='Doctor', required=True)
    appointment_type = fields.Selection([
        ('in_person', 'In-person'),
        ('virtual', 'Virtual')
    ], string='Appointment Type', required=True)
