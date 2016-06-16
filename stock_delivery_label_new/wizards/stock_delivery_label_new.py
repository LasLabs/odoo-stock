# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class StockDeliveryLabelNew(models.TransientModel):
    """ Create a new stock delivery label.
    Not useful on its own, but provides a unified hook for external carrier
    connector interfaces.
    This wizard should be monitored by external connectors for creation. They
    can then implicitly determine the interface to purchase shipment over
    based on the ``rate_id`` attribute
    """

    _name = "stock.delivery.label.new"
    _description = 'Stock Delivery Label New'

    picking_id = fields.Many2one(
        string='Stock Picking',
        comodel_name='stock.picking',
        readonly=True,
        default=lambda s: s.env.context.get('active_id'),
    )
    group_id = fields.Many2one(
        string='Delivery Group',
        comodel_name='stock.delivery.group',
        required=True,
        domain="[('picking_id', '=', picking_id), ('state', '=', 'new')]",
    )
    rate_id = fields.Many2one(
        string='Rate',
        comodel_name='stock.delivery.rate',
        required=True,
        domain="[('group_id', '=', group_id)]",
    )

    @api.multi
    def action_trigger_label(self):
        """ Inherit this in connector interfaces if custom processing
        is needed before label purchase. No label is actually created
        in this method though, as the connector should fire and use the
        rate_id for its processing.
        """
        return {'type': 'ir.actions.act_window_close'}
