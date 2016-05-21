# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestStockDeliveryGroup(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestStockDeliveryGroup, self).setUp(*args, **kwargs)

    def new_record(self):
        self.picking_id = self.env['stock.picking'].create({
            'location_dest_id': self.env['stock.location'].search([])[0].id,
            'location_id': self.env['stock.location'].search([])[0].id,
            'picking_type_id':
                self.env['stock.picking.type'].search([])[0].id,
        })
        return self.env['stock.delivery.group'].create({
            'picking_id': self.picking_id.id,
        })

    def new_operation(self, group_id):
        return self.env['stock.delivery.operation'].create({
            'group_id': group_id.id,
        })

    def test_last_operation_id(self):
        rec_id = self.new_record()
        self.new_operation(rec_id)
        op_id = self.new_operation(rec_id)
        self.assertEqual(
            op_id, rec_id.last_operation_id,
            'Did not get proper last op. Expect %s, Got %s' % (
                op_id, rec_id.last_operation_id,
            )
        )
