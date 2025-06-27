from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'
    
    name = fields.Char('Name', required=True)
    biography = fields.Text('Biography')
    book_ids = fields.Many2many(
        'library.book', 
        string='Books Authored'
    )
    book_count = fields.Integer(
        'Number of Books',
        compute='_compute_book_count'
    )
    
    def _compute_book_count(self):
        for author in self:
            author.book_count = len(author.book_ids)