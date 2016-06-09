# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class StockDeliveryGroup(models.Model):
    _name = 'stock.delivery.group'
    _inherit = ['stock.delivery.group', 'mail.thread']
