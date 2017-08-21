# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Portal for Purchases',
    'category': 'Website',
    'summary': 'Add your purchase orders in the frontend portal',
    'version': '1.0',
    'description': """
Display purchase orders on your website. Customers will be able to access their purchase orders in their own portal, see their state and communicate with salesmen.
        """,
    'depends': [
        'purchase',
        'website',
        'portal',
    ],
    'data': [
    ],
    'installable': True,
}
