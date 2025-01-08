import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HHDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = ['hr.hospital.person.mixin']
    _description = 'Doctor'
    name = fields.Char(
        compute='_compute_name',
        store=True,
    )
    d_is_intern = fields.Boolean()
    d_main_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Main Doctor",
        domain=[('d_is_intern', '=', False)],
    )
    d_main_doctor_id_specialty = fields.Many2one(
        related='d_main_doctor_id.d_specialty_id',
        string="Specialty main doctor",
    )
    d_specialty_id = fields.Many2one(
        comodel_name='hr.hospital.specialty',
        string="Specialty",
    )
    d_intern_ids = fields.One2many(comodel_name='hr.hospital.doctor', inverse_name='d_main_doctor_id',
                                   string="Subordinate Interns",)
    d_patient_ids = fields.One2many(comodel_name='hr.hospital.patient', inverse_name='personal_doctor_id',
                                    string="Patients",)
    d_visit_ids = fields.One2many(comodel_name='hr.hospital.visit', inverse_name='doctor_id',
                                    string="Visits",)

    @api.depends('d_is_intern')
    def _onchange_d_is_intern(self):
        self.d_main_doctor_id = False

    @api.constrains('d_main_doctor_id')
    def _check_d_main_doctor_id(self):
        for record in self:
            if record.d_main_doctor_id.d_is_intern:
                raise ValidationError("You cannot list an intern as a main doctor!")
            if record.d_is_intern and len(record.d_intern_ids) > 0:
                raise ValidationError("The doctor has a subordinate intern! You can't list him as an intern.")

    @api.depends('first_name','last_name')
    def _compute_name(self):
        for doctor in self:
            doctor.name = f'{doctor.first_name} {doctor.last_name}'

    def create_visit_for_doctor(self):
        self.ensure_one()
        return {
            'name': 'Create visit',
            'type': 'ir.actions.act_window',
            'res_model': 'hr.hospital.visit',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {
                'default_doctor_id': self.id,
                       },
                }
