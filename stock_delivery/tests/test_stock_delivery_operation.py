# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestStockDeliveryOperation(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestStockDeliveryOperation, self).setUp(*args, **kwargs)

    def new_record(self):
        self.picking_id = self.env['stock.picking'].create({
            'location_dest_id': self.env['stock.location'].search([])[0].id,
            'location_id': self.env['stock.location'].search([])[0].id,
            'picking_type_id':
                self.env['stock.picking.type'].search([])[0].id,
        })
        self.group_id = self.env['stock.delivery.group'].create({
            'picking_id': self.picking_id.id,
        })
        self.date = '2015-01-02 00:10:20'
        self.state = 'in_transit'
        return self.env['stock.delivery.operation'].create({
            'group_id': self.group_id.id,
            'date': self.date,
            'state': self.state,
        })

    def test_name_get(self):
        rec_id = self.new_record()
        expect = '[{date}] {state}'.format(
            date=self.date,
            state=self.state,
        )
        self.assertEqual(
            expect, rec_id.name_get()[0][1],
            'Did not get name w/ state. Expect %s, Got %s' % (
                expect, rec_id.name_get()[0][1],
            )
        )
