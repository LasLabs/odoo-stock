# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields
from openerp import api


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    @api.onchange('length', 'height', 'width', 'dimensional_uom_id')
    def onchange_calculate_volume(self):
        if (
                not self.length or not self.height or
                not self.width or not self.dimensional_uom_id
                ):
            return False

        length_m = self.convert_to_meters(self.length, self.dimensional_uom_id)
        height_m = self.convert_to_meters(self.height, self.dimensional_uom_id)
        width_m = self.convert_to_meters(self.width, self.dimensional_uom_id)
        self.volume = length_m * height_m * width_m

    def convert_to_meters(self, measure, dimensional_uom):
        uom_meters = self.env['product.uom'].search([('name', '=', 'm')])

        return self.env['product.uom']._compute_qty_obj(
            from_unit=dimensional_uom,
            qty=measure,
            to_unit=uom_meters)

    @api.model
    def _get_dimension_uom_domain(self):
        return [
            ('category_id', '=', self.env.ref('product.uom_categ_length').id)
        ]

    length = fields.Float('Length')
    width = fields.Float('Width')
    height = fields.Float('Height')
    dimensional_uom_id = fields.Many2one(
        'product.uom',
        'Dimension UoM',
        domain=_get_dimension_uom_domain,
        help='UoM for package length, height, width')
