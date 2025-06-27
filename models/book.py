from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    
    name = fields.Char('Title', required=True, tracking=True)
    author_ids = fields.Many2many(
        'library.author', 
        string='Authors',
        tracking=True
    )
    genre = fields.Selection([
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('biography', 'Biography'),
        ('children', 'Children'),
        ('science', 'Science'),
        ('history', 'History'),
    ], string='Genre')
    numOfcopys = fields.Integer('Number of Copys')
  
    
    