# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock Delivery Label New",
    "summary": "Adds a label generation wizard to stock pickings. Meant for "
               "use with carrier connector interfaces.",
    "version": "9.0.1.0.0",
    "category": "Hidden",
    "website": "https://laslabs.com/",
    "author": "LasLabs",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock_delivery"
    ],
    "data": [
        'wizards/stock_delivery_label_new_view.xml',
    ],
}
