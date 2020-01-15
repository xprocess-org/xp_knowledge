# -*- coding: utf-8 -*-
{
    'name': "Knowledge",
    'summary': """Controlled knowledge documentation app""",
    'description': """
        This module developed mainly to support quality system documentation like ISO 9001
        but for better utilization it designed to support any kind of controlled documentation within the company
    """,

    'author': "xprocess.org",
    'website': "https://github.com/xprocess-org/xp_knowledge",
    "license": "LGPL-3",

    'category': 'Knowledge',
    'version': '13.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/knowledge_security.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
}
