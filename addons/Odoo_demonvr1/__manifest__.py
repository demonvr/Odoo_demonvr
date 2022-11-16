# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'File Upload',
    'version': '1.0',
    'category': 'Productivity/Productivity',
    'summary': 'File Upload',
    'application': True,
    'depends': ['base'],
    'auto_install': True,
    'data': [
        'views/file_upload_menu.xml',
        'security/ir.model.access.csv'
    ],
}
