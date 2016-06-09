# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestStockDeliveryGroupLine(TransactionCase):

    def test_inherits_mail_thread(self):
        model_obj = self.env['stock.delivery.group.line']
        self.assertTrue(hasattr(model_obj, 'message_new'))