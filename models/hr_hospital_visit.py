import logging
from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'

    state = fields.Selection(
        selection=[('plan', 'Заплановано'),
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
        required=True
    )
    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string="Patient",
        required=True
    )
    visit_date = fields.Date(
        compute='_compute_visit_date',
        store=True,
    )
    visit_datetime = fields.Datetime(required=True)
    visited_datetime = fields.Datetime(
        compute='_compute_state',
        store=True,
    )
    diagnosis_ids = fields.One2many(comodel_name='hr.hospital.diagnosis', inverse_name='visit_id',
                                    string="diagnosis", )

    _sql_constraints = [

        ('doctor_patient_day_uniq', 'unique (doctor_id,patient_id,visit_date)',
         'On this date, this patient is already registered with this doctor !'),
        ('doctor_datetime_uniq', 'unique (doctor_id,visit_datetime)',
         'On this date and time, this doctor is already busy !')

    ]

    @api.depends('doctor_id', 'visit_date', 'visit_time')
    def _check_status(self):
        for record in self:
            if record.status == 'done':
                raise UserError("Visit is done")

    @api.constrains('active')
    def _check_status(self):
        for record in self:
            if not record.active and len(record.diagnosis_ids):
                raise ValidationError("You cannot archived visits for which you have already been diagnosed")

    @api.depends('visit_datetime')
    def _compute_visit_date(self):
        for visit in self:
            visit.visit_date = visit.visit_datetime.date()

    @api.depends('state')
    def _compute_state(self):
        for visit in self:
            if visit.state == 'done':
                visit.visited_datetime = fields.Datetime().now()
            else:
                visit.visited_datetime = False

    @api.ondelete(at_uninstall=False)
    def _unlink_except_diagnosis(self):
        if len(self.mapped('diagnosis_ids')):
            raise UserError(_("You cannot delete visits for which you have already been diagnosed"))

