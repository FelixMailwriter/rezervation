# -*- coding: utf-8 -*-
{
    'name': "rezervation",

    'summary': """
        App for managing of booking for a little hotel""",

    'description': """
        This app make managing of the little hotel much easier. It helps you to count all your clients and 
        booking. 
    """,

    'author': "ComLib",
    'website': "http://www.comlib.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/flat.xml',
        'views/amenity.xml',
        'views/user.xml',
        'views/city.xml',
        'views/country.xml',
        'views/partners.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'autoinstall': False
}
