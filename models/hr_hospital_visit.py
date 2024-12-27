import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError,UserError

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'

    name = fields.Char()
    state = fields.Selection(
        [('plan', 'Заплановано'),
         ('close', 'Скасовано'),
         ('done', 'Завершено')],
        default="plan",
        string='State',
    )

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
    visit_date = fields.Date(
        compute='_compute_visit_date',
        store=True,
    )
    visit_datetime = fields.Datetime()
    visited_datetime = fields.Datetime()
    diagnosis_ids = fields.One2many('hr.hospital.diagnosis', 'visit_id',
                                   string="diagnosis", )

    _sql_constraints = [

        ('doctor_patient_day_uniq', 'unique (doctor_id,patient_id,visit_date)', 'On this date, this patient is already registered with this doctor !')

    ]

    @api.constrains('doctor_id', 'visit_date', 'visit_time')
    def _check_status(self):
        for record in self:
            if record.status == 'done':
                raise ValidationError("Visit is done")

    @api.constrains('active')
    def _check_status(self):
        for record in self:
            if record.active and len(record.diagnosis_ids):
                raise ValidationError("You cannot archived visits for which you have already been diagnosed")

    @api.depends('visit_datetime')
    def _compute_visit_date(self):
        for visit in self:
            visit.visit_date = visit.visit_datetime.date()

    @api.ondelete(at_uninstall=False)
    def _unlink_except_diagnosis(self):
        if len(self.mapped('diagnosis_ids')):
            raise UserError(_("You cannot delete visits for which you have already been diagnosed"))

