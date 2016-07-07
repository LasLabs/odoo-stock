# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Website Stock Picking",
    "summary": "Add website workflows for stock picking.",
    "version": "9.0.0.1.0",
    "category": "Website",
    "website": "https://laslabs.com/",
    "author": "LasLabs",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "website",
    ],
    "data": [
        'wizards/website_stock_picking_wizard_template.xml',
    ],
    'demo': [
        'demo/website_stock_picking_demo.xml',
    ],
}
