# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestProductPackaging(TransactionCase):

    def setUp(self):
        super(TestProductPackaging, self).setUp()
        self.package = self.env['product.packaging'].new()
        self.uom_m = self.env['product.uom'].search([('name', '=', 'm')])
        self.uom_cm = self.env['product.uom'].search([('name', '=', 'cm')])

    def test_it_computes_volume_in_cm(self):
        self.package.length = 10.
        self.package.height = 200.
        self.package.width = 100.
        self.package.dimensional_uom_id = self.uom_cm
        self.package.onchange_calculate_volume()
        self.assertAlmostEqual(
            0.2,
            self.package.volume
        )

    def test_it_computes_volume_in_meters(self):
        self.package.length = 6.
        self.package.height = 2.
        self.package.width = 10.
        self.package.dimensional_uom_id = self.uom_m
        self.package.onchange_calculate_volume()
        self.assertAlmostEqual(
            120,
            self.package.volume
        )

    def test_calculate_volume_none_dimension(self):
        '''Tests _calculate_volume for empty dimensions'''
        self.package.length = None
        self.package.height = None
        self.package.width = None
        self.package.dimensional_uom_id = None
        self.assertFalse(
            self.package.onchange_calculate_volume(),
            'Should return False if falsey values present',
        )
