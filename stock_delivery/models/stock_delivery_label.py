# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields
import openerp.addons.decimal_precision as dp


class StockDeliveryLabel(models.Model):
    _name = 'stock.delivery.label'
    _description = 'Stock Delivery Label'

    picking_id = fields.Many2one(
        string='Stock Picking',
        comodel_name='stock.picking',
        required=True,
    )
    group_ids = fields.One2many(
        string='Delivery Groups',
        comodel_name='stock.delivery.group',
        inverse_name='label_id',
    )
    date_generated = fields.Datetime(
        required=True,
        default=lambda s: fields.Datetime.now(),
    )
    currency_id = fields.Many2one(
        string='Currency',
        comodel_name='res.currency',
        required=True,
    )
    rate = fields.Float(
        digits=dp.get_precision('Product Price'),
        required=True,
    )
    img_label = fields.Binary(
        attachment=True,
        required=True,
    )
    service_id = fields.Many2one(
        string='Carrier Service',
        comodel_name='delivery.carrier',
        related='picking_id.carrier_id',
    )
    partner_id = fields.Many2one(
        string='Carrier Company',
        comodel_name='res.partner',
        related='service_id.partner_id',
    )
    state = fields.Selection([
        ('valid', 'Valid'),
        ('cancel', 'Cancelled'),
    ],
        default='valid',
    )
