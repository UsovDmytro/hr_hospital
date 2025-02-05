import logging

from odoo import models, fields, _

_logger = logging.getLogger(__name__)


class HHDisease(models.Model):
    """
    Disease
    """
    _name = 'hr.hospital.disease'
    _description = _('Disease')

    name = fields.Char()

    active = fields.Boolean(
        default=True, )

    parent_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string=_('Parent Disease'),
        index=True,
        ondelete='cascade')



