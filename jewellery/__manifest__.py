# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Noipunno Jewellery ',
    'version': '15.0.1.0.0',
    'category': 'Gold',
    'description': """
        for local and hole sell business
    """,
    'author': 'Noipunno Info-tech',
    'maintainer': 'Noipunno Info-tech',
    'summary': ' ',
    'website': 'noipunnoinfotech@gmai.com',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'views/order_view.xml',
        'views/rate.xml',
        # 'views/payment_view.xml',
        'security/ir.model.access.csv',

    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
}
