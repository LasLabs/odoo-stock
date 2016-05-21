# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    delivery_rate_ids = fields.One2many(
        string='Delivery Rates',
        comodel_name='stock.delivery.rate',
        inverse_name='picking_id',
    )
    delivery_label_ids = fields.One2many(
        string='Delivery Labels',
        comodel_name='stock.delivery.label',
        inverse_name='picking_id',
    )
    delivery_group_ids = fields.One2many(
        string='Delivery Groups',
        comodel_name='stock.delivery.group',
        inverse_name='picking_id',
    )
