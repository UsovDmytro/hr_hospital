import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHPerson(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person'
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    photo = fields.Image(
        max_width=512,
        max_height=512,
    )
    gender = fields.Selection(
        selection=[('male', 'male'),
                   ('female', 'female'),
                   ('other', 'other')],
        # required=True,
    )
    phone = fields.Char()
