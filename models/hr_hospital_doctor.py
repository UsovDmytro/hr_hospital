import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )

    intern = fields.Boolean()

    main_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Main Doctor",
    )

    intern_ids = fields.One2many('hr.hospital.doctor', 'main_doctor_id',
                                 string="Subordinate Interns",)
