import logging

from odoo import models, fields, _

_logger = logging.getLogger(__name__)


class HHSpecialty(models.Model):
    """
    Specialty
    """
    _name = 'hr.hospital.specialty'
    _description = _('Specialty')

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
