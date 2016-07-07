# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from collections import defaultdict

from openerp import api, models, fields


class WebsiteStockPickingWizard(models.TransientModel):
    _name = "website.stock.picking.wizard"
    _description = 'Website Stock Picking Wizard'

    search_query = fields.Char()
    picking_type = fields.Selection([
        ('incoming', 'Incoming'),
        ('outgoing', 'Outgoing'),
        ('internal', 'Internal'),
    ])
    picking_state = fields.Selection([
        ('draft', 'Draft'),
        ('cancel', 'Cancelled'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting Availability'),
        ('partially_available', 'Partially Available'),
        ('assigned', 'Available'),
        ('done', 'Done'),
    ],
        default='assigned',
    )
    company_id = fields.Many2one(
        string='Company',
        comodel_name='res.company',
        default=lambda s: s.env.user.company_id.id,
        required=True,
    )
    picking_ids = fields.Many2many(
        string='Pickings',
        comodel_name='stock.picking',
    )

    @api.multi
    def _get_domain(self):
        self.ensure_one()
        domain = [
            ('company_id', '=', self.company_id.id),
        ]
        if self.search_query:
            domain.append(('name', '=', self.search_query))
        if self.picking_type:
            domain.append(('picking_type_id.code', '=', self.picking_type))
        if self.picking_state:
            domain.append(('state', '=', self.picking_state))
        return domain

    @api.model
    def create(self, vals):
        rec_id = super(WebsiteStockPickingWizard, self).create(vals)
        rec_id.action_search()
        return rec_id

    @api.multi
    def action_search(self):
        for rec_id in self:
            pick_ids = self.env['stock.picking'].search(self._get_domain())
            rec_id.write({
                'picking_ids': [(6, 0, pick_ids.ids)]
            })

    @api.multi
    def action_process_form(self, form_values):
        self.write(
            self._process_form_vals(form_values)
        )

    @api.model
    def _process_form_vals(self, form_values):
        field_map = defaultdict(dict)
        for name, value in form_values.iteritems():
            try:
                op_id, field = name.split('.', 1)
            except ValueError:
                continue
            field_map[op_id][field] = value
        return {
            'pack_operation_product_ids': [
                (1, k, v) for k, v in field_map.iteritems()
            ]
        }
