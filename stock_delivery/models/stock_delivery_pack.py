# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields
import openerp.addons.decimal_precision as dp


class StockDeliveryPack(models.Model):
    _name = 'stock.delivery.pack'
    _description = 'Stock Delivery Pack'
    _inherits = {'stock.delivery.pack.template': 'pack_template_id'}

    pack_template_id = fields.Many2one(
        name='Template',
        comodel_name='stock.delivery.pack.template',
        ondelete='cascade',
        required=True,
    )
    weight = fields.Float(
        digits=dp.get_precision('Stock Weight'),
    )
    weight_uom_id = fields.Many2one(
        string='Weight Unit',
        comodel_name='product.uom',
    )
