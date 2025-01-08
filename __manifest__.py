{
    'name': 'Hospital HR',
    'summary': '',
    'author': 'Usov Dmytro',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.0.0',
    'depends': ['base',],
    'external_dependencies': {
        'python': [],
    },
    'data': [

        'security/ir.model.access.csv',
        'wizard/hr_hospital_change_doctor_wizard_view.xml',
        'wizard/hr_hospital_change_patient_wizard_view.xml',
        'wizard/hr_hospital_diagnosis_wizard_view.xml',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_visit_views.xml',
        'views/hr_hospital_specialty_views.xml',
        'views/hr_hospital_diagnosis_views.xml',

        'data/hr_hospital_disease_data.xml',

    ],
    'demo': [
        'demo/hr_hospital_specialty_demo.xml',
        'demo/hr_hospital_doctor_demo.xml',
        'demo/hr_hospital_patient_demo.xml',
        'demo/hr_hospital_visit_demo.xml',
        'demo/hr_hospital_diagnosis_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
