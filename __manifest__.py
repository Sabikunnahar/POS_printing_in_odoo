# -*- coding: utf-8 -*-
{
    'name': 'POS Receipt',
    'version': '1.0',
    'summary': 'POS printing',
    'sequence': 10,
    'description': """POS printing
    Bahmni Sale
====================
""",
    'category': 'Sales',
    'website': [],
    'images': [],
    'depends': ['base', 'purchase'],
    'data': [
        'reports/report.xml',
        'reports/report_tamplate.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
