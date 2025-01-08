import logging
from datetime import date

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HHPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = ['hr.hospital.person.mixin']
    _description = 'Patient'
    name = fields.Char(
        compute='_compute_name',
        store=True,
    )
    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Personal doctor",
    )
    birthday = fields.Date()
    passport = fields.Char()
    contact_person = fields.Char()
    age = fields.Integer(
        compute='_compute_age',
    )
    diagnosis_ids = fields.One2many(comodel_name='hr.hospital.diagnosis', inverse_name='patient_id',
                                    string="diagnosis patient",)

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for patient in self:
            if fields.Date.to_date(patient.birthday) is None:
                patient.age = 0
                continue
            age = today.year - patient.birthday.year
            if (today.month, today.day) < (patient.birthday.month, patient.birthday.day):
                age -= 1
            patient.age = age

    def _compute_name(self):
        for patient in self:
            patient.name = f'{patient.first_name} {patient.last_name}'

    def create_visit_for_patient(self):
        self.ensure_one()

        context_dict = {'default_patient_id': self.id}
        if self.personal_doctor_id:
            context_dict['default_doctor_id'] = self.personal_doctor_id.id

        return {
            'name': 'Create visit',
            'type': 'ir.actions.act_window',
            'res_model': 'hr.hospital.visit',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': context_dict,
                }

    def history_visit_for_patient(self):
        self.ensure_one()

        return {
            'name': f'History visit for {self.name}',
            'type': 'ir.actions.act_window',
            'res_model': 'hr.hospital.visit',
            'view_mode': 'tree',
            'view_type': 'tree',
            'target': 'new',
            'domain': [('patient_id', '=', self.id)],
                }
