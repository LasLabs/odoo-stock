# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Delivery Thread',
    'version': '9.0.1.0.0',
    'author': 'LasLabs,
    'category': 'Stock',
    'depends': [
        'stock_delivery',
    ],
    'website': 'https://laslabs.com/',
    'license': 'AGPL-3',
    'data': [
        'views/stock_delivery_group_view.xml',
        'views/stock_delivery_group_line_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
