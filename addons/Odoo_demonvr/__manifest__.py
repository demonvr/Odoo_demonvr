# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Test field for sales module',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
This module contains test field.
    """,
    'depends': ['sale'],
    'auto_install': True,
    'data': [
        'views/sale_order_view.xml',
        'views/templates.xml'
    ],
}
