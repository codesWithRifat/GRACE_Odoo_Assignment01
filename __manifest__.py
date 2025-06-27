{
    'name':'library management system',
    'version': '16.0.0.0.',
    'category' : 'Tools',
    'summary': 'A basic custom module',
    'description': 'This is a simple custom module',
    'author': 'Rifat',
    'depends': ['base'],
    'data':[
          'security/ir.model.access.csv',
          'views/library.xml',
          'views/book.xml',
          'views/author_view.xml',
          'views/borrow_view.xml',
    ],
    'installable': True,
    'application': True,
}