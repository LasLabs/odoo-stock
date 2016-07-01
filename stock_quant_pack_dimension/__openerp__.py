# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Quant Package Dimension',
    'summary': 'Provide dimensions on packaging',
    'version': '9.0.1.0.0',
    'category': 'Hidden',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale_stock',
    ],
    'data': [
        'views/product_packaging_view.xml',
        'views/stock_quant_package_view.xml',
    ],
}
