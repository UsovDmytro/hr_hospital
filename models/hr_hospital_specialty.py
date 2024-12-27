import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHSpecialty(models.Model):
    _name = 'hr.hospital.specialty'
    _description = 'Specialty'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
