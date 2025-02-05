
from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_hospital_doctor = self.env.ref(
            'hr_hospital.group_hospital_doctor')
        self.group_hospital_admin = self.env.ref(
            'hr_hospital.group_hospital_admin')
        self.hospital_doctor_user = self.env['res.users'].create({
            'name': 'Doctor',
            'login': 'doctor',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_hospital_doctor.id)],
        })
        self.hospital_admin = self.env['res.users'].create({
            'name': 'Hospital Admin',
            'login': 'hospital_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_hospital_admin.id)],
        })
        self.doctor = self.env['hr.hospital.doctor'].create({
            'first_name': 'Demo',
            'last_name': 'Doctor',
            'user_id': self.hospital_doctor_user.id,
        })
        self.another_doctor = self.env['hr.hospital.doctor'].create({
            'first_name': 'Demo',
            'last_name': 'Doctor 2',
        })
        self.patient = self.env['hr.hospital.patient'].create({
            'first_name': 'Demo',
            'last_name': 'Patient',
        })