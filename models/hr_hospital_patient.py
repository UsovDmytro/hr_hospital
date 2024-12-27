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

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for patient in self:
            if patient.birthday is None:
                continue
            age = today.year - patient.birthday.year
            if (today.month, today.day) < (patient.birthday.month, patient.birthday.day):
                age -= 1
            patient.age = age

    def _compute_name(self):
        for patient in self:
            patient.name = f'{patient.first_name} {patient.last_name}'