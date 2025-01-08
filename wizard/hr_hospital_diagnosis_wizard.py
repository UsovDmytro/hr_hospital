import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HHDiagnosisWizard(models.TransientModel):
    _name = 'hr.hospital.diagnosis.wizard'
    _description = 'Diagnosis wizard'

    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor',
        string='Doctors',
    )
    disease_ids = fields.Many2many(
        comodel_name='hr.hospital.disease',
        string='Diseases',
    )
    date_from = fields.Date()
    date_to = fields.Date()

    def action_refresh_pivot(self):
        domain = []
        if self.doctor_ids:
            domain.append([('visit_id.doctor_id', 'in', self.doctor_ids.ids)])
        if self.disease_ids:
            domain.append([('disease_id', 'in', self.disease_ids.ids)])
        if self.date_from:
            domain.append([('visit_id.visit_date', '>=', self.date_from)])
        if self.date_to:
            domain.append([('visit_id.visit_date', '<=', self.date_to)])

        return {
            'type': 'ir.actions.act_window',
            'name': 'Pivot Report',
            'res_model': 'hr.hospital.diagnosis',
            'view_mode': 'pivot',
            'target': 'new',
            'domain': domain
        }
