{
    'name': 'eCommerce',
    'version': '1.0.0',
    'sequence': -100,
    'category': 'Theme/Creative',
    'summary': 'Ecommerce Management System',
    'description': """Ecommerce Management System""",
    'depends': ['website'],
    'data': [

        'views/test_page.xml',
        # 'views/odoo_theme.xml',
        # 'views/template.xml',
        'views/product_page.xml',
        'views/layout.xml',
        'views/about_page.xml',
        'views/snippets/test_snippet.xml',
        'views/snippets/custom_snippet.xml',

    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_frontend': [
            '/theme_name/static/src/scss/style.scss',
            # 'theme_name/static/src/css/img/test_thumbnail.png',
            # '/theme_name/static/src/css/odoo_theme.css',
        ],
    },
}
