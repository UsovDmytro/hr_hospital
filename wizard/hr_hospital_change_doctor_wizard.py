import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HHChangeDoctor(models.TransientModel):
    _name = 'hr.hospital.change.doctor.wizard'
    _description = 'Change personal doctor'

    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
    )
    d_patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',

        string='Patients',)

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self.env.context.get('active_id'):
            doctor_id = self.env['hr.hospital.doctor'].browse(self.env.context.get('active_id'))
            res['personal_doctor_id'] = doctor_id.id
            res['res_partner_ids'] = [(6, 0, doctor_id.d_patient_ids.ids)]
        return res

    @api.onchange('personal_doctor_id')
    def _onchange_personal_doctor_id(self):
        self.d_patient_ids = [(6, 0, self.personal_doctor_id.d_patient_ids.ids)]

    def change_doctor(self):
        self.personal_doctor_id.d_patient_ids = self.d_patient_ids
