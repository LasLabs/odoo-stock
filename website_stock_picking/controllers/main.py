# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http
from openerp.http import request


import logging
_logger = logging.getLogger(__name__)


class WebsiteSale(http.Controller):

    @http.route(
        ['/website_stock_picking/'],
        type='http',
        auth="public",
        website=True,
        methods=["GET"],
    )
    def show_picking_search(self, **kwargs):

        wizard_obj = request.env['website.stock.picking.wizard']
        wizard_id = wizard_obj.search([
            ('create_uid', '=', request.env.user.id),
        ],
            limit=1,
        )
        tpl_vals = {
            'errors': kwargs.get('errors', [])
        }

        if kwargs:

            search_vals = {
                'search_query': kwargs.get('search_query'),
            }
            if not wizard_id:
                wizard_id = wizard_obj.create(search_vals)
            else:
                wizard_id.write(search_vals)

            tpl_vals.update({
                'wizard': wizard_id,
                'pickings': wizard_id.picking_ids,
            })

            if len(wizard_id.picking_ids) == 1:
                return self.show_picking_detail(
                    wizard_id.picking_ids[0].id,
                )

        else:
            if not wizard_id:
                wizard_id = wizard_obj.create({})
                wizard_id.action_search()
            tpl_vals.update({
                'wizard': wizard_id,
                'pickings': wizard_id.picking_ids,
            })

        return request.website.render(
            "website_stock_picking.picking_search",
            tpl_vals,
        )

    @http.route(
        ['/website_stock_picking/<int:picking_id>'],
        type='http',
        auth='public',
        website=True,
        methods=['GET', 'POST'],
    )
    def show_picking_detail(self, picking_id, **kwargs):

        _logger.debug(kwargs)

        tpl_vals = {
            'errors': kwargs.get('errors', []),
        }

        picking_id = request.env['stock.picking'].browse(picking_id)
        if not picking_id:
            return self.show_picking_search(
                errors=['No picking was found']
            )

        tpl_vals.update({'picking': picking_id})
        return request.website.render(
            "website_stock_picking.picking_detail",
            tpl_vals,
        )
