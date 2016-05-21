# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields
import openerp.addons.decimal_precision as dp


class StockDeliveryRate(models.Model):
    _name = 'stock.delivery.rate'
    _description = 'Stock Delivery Rate'

    picking_id = fields.Many2one(
        string='Stock Picking',
        comodel_name='stock.picking',
        required=True,
    )
    partner_id = fields.Many2one(
        string='Carrier Company',
        comodel_name='res.partner',
        related='service_id.partner_id',
    )
    service_id = fields.Many2one(
        string='Carrier Service',
        comodel_name='delivery.carrier',
        required=True,
    )
    date_generated = fields.Datetime(
        required=True,
        default=lambda s: fields.Datetime.now(),
    )
    rate_currency_id = fields.Many2one(
        string='Rate Currency',
        comodel_name='res.currency',
        required=True,
    )
    rate = fields.Float(
        digits=dp.get_precision('Product Price'),
        required=True,
    )
    retail_rate = fields.Float(
        digits=dp.get_precision('Product Price'),
    )
    retail_rate_currency_id = fields.Many2one(
        string='Retail Rate Currency',
        comodel_name='res.currency',
    )
    list_rate = fields.Float(
        digits=dp.get_precision('Product Price'),
    )
    list_rate_currency_id = fields.Many2one(
        string='List Rate Currency',
        comodel_name='res.currency',
    )
    delivery_days = fields.Integer(required=True)
    date_delivery = fields.Datetime(
        string='Est Delivery Date',
        required=True,
    )
    is_guaranteed = fields.Boolean(
        string='Date is Guaranteed?',
    )
