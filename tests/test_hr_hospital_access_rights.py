import datetime

from odoo.addons.school_lesson_6_4.tests.common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'library', 'access')
class TestAccessRights(TestCommon):

    def test_01_library_user_access_rights(self):
        self.env['hr.hospital.visit'].with_user(self.hospital_doctor_user).create(
            {'doctor_id': self.doctor.id,
             'patient_id': self.patient.id,
             'visit_datetime': datetime.datetime.now(),
             })
        with self.assertRaises(AccessError):
            self.env['hr.hospital.visit'].with_user(self.hospital_doctor_user).create(
                {'doctor_id': self.another_doctor.id,
                 'patient_id': self.patient.id,
                 'visit_datetime': datetime.datetime.now(),
                 })
