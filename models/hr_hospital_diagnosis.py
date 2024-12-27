import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HHDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string="Visit",
    )
    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string="Disease",
    )
    description = fields.Text()
    approved = fields.Boolean()

    @api.onchange('visit_id')
    def _onchange_visit_id(self):
        self.approved = not self.visit_id.doctor_id.d_is_intern
