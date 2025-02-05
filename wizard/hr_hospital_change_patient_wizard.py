import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class HHChangePatient(models.TransientModel):
    """
    Change patient for doctor
    """
    _name = 'hr.hospital.change.patient.wizard'
    _description = _('Change patient for doctor')

    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string=_('Doctor'),
    )
    d_patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',
        readonly=True,
        string=_('Patients'),)

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self.env.context.get('active_ids'):
            d_patient_ids = self.env['hr.hospital.doctor'].browse(self.env.context.get('active_ids'))
            res['d_patient_ids'] = [(6, 0, d_patient_ids.ids)]
        return res

    def change_patient(self):
        """
         changes the doctor's patient list
         :return:
         """
        self.personal_doctor_id.d_patient_ids = self.d_patient_ids
