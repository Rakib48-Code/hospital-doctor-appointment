{
    'name': 'Appointment',
    'version': '16.0.1.0.2',
    'summary': 'Appointment Module In odoo16',
    'description': 'Appointment Module In odoo16',
    'sequence': 1,
    'category': 'Appointment',
    'author': 'Rakib',
    'website': 'www.example.com',
    'license': 'AGPL-3',
    'depends': ['hr','mail'],
    'data': [
        # security
        'security/ir.model.access.csv',

        # data
        # 'data/sequence.xml',
        # 'data/schedule_sequence.xml',

        # views
        'views/menu.xml',
        'views/patient_appointment.xml',
        'views/schedule.xml',

        # report
        'report/report_template.xml',
        'report/report_action.xml',
    ],
    'demo': [],
    'installable': True,
    'application' : True,
    'auto_install': False,
}