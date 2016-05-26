# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class StockDeliveryPack(models.Model):
    _name = 'stock.delivery.pack'
    _description = 'Stock Delivery Pack'
    _inherit = 'stock.delivery.pack.template'
    _inherits = {'stock.quant.package': 'quant_pack_id'}

    group_id = fields.Many2one(
        name='Delivery Group',
        comodel_name='stock.delivery.group',
    )
    pack_template_id = fields.Many2one(
        name='Package Template',
        comodel_name='stock.delivery.pack.template',
    )
    quant_pack_id = fields.Many2one(
        name='Quant Pack',
        comodel_name='stock.quant.package',
        ondelete='cascade',
        required=True,
    )

    @api.onchange('pack_template_id')
    def _onchange_pack_template_id(self):
        for key, val in self.read()[0].iteritems():
            setattr(self, key, val)
