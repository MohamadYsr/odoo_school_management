# -*- coding: utf-8 -*-
{
    'name': "School MS",

    'summary': """
        This module or application represent School Management System and operations""",

    'description': """
        School Management System
    """,

    'author': "Mohamad Al-ahmad",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'portal', 'mail', 'utm', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data.xml',
        'views/views.xml',
        'views/level.xml',
        'views/material.xml',
        'views/setting.xml',
        'views/templates.xml',
        'report/report.xml',
        'wizard/report_student_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
