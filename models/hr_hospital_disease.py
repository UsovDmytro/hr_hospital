import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHDisease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease'
    # _parent_name = "parent_id"
    # _parent_store = True

    name = fields.Char()

    active = fields.Boolean(
        default=True, )

    # parent_id = fields.Many2one(
    #     'hr.hospital.disease',
    #     'Parent Disease',
    #     index=True,
    #     ondelete='cascade')

