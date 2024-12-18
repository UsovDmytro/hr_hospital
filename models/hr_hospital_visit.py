import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Doctor",
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string="Patient",
    )

    visit_datetime = fields.Datetime()
