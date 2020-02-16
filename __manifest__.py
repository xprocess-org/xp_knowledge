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
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/knowledge_groups.xml',
        'security/ir.model.access.csv',
        'views/knowledge_menus.xml',
        'views/knowledge_assets.xml',
        'views/knowledge_package_views.xml',
        'views/knowledge_document_views.xml',
        'views/knowledge_change_request_item_views.xml',
        'views/knowledge_change_request_views.xml',
        'views/knowledge_distribution_list_views.xml',
        'views/knowledge_document_type_views.xml',
        'data/knowledge.document.type.csv',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
}
