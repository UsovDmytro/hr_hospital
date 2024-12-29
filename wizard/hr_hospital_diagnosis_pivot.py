import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HHDiagnosisPivot(models.TransientModel):
    _name = 'hr.hospital.diagnosis.pivot'
    _description = 'Diagnosis pivot'

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
    )
    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string='Disease',
    )
    date_from = fields.Date()
    date_to = fields.Date()

    def get_diagnosis(self):
        found_diagnosis = self.env['hr.hospital.diagnosis'].search([])
        if self.doctor_id:
            found_diagnosis = found_diagnosis.filtered_domain([('visit_id.doctor_id', '=', self.doctor_id.id)])
        if self.disease_id:
            found_diagnosis = found_diagnosis.filtered_domain([('disease_id', '=', self.disease_id.id)])
        if self.date_from:
            found_diagnosis = found_diagnosis.filtered_domain([('visit_id.visit_date', '>=', self.date_from)])
        if self.date_to:
            found_diagnosis = found_diagnosis.filtered_domain([('visit_id.visit_date', '<=', self.date_to)])
        return found_diagnosis
