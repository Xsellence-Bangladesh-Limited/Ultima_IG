{
    'name' : 'Ultima',
    'version' : '1.0',
    'summary': 'Ultima website module',
    'sequence': 200,
    'description': """Developed by Xsellence Bangladesh Limited.""",
    'category': '',
    'website': '',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/ashik/views.xml',
        'views/razzak/views.xml',
        'views/ashik/views_menu.xml',
        'views/razzak/views_menu.xml',

        # Templates
        'templates/base_layout.xml',
        'templates/ashik/contact_us.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
