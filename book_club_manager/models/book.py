from odoo import models, fields, api

class BookClubBook(models.Model):
    _name = 'book.club.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    published_date = fields.Date(string='Published Date')
    genre = fields.Selection([
        ('islamic', 'Islamic'),
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('fantasy', 'Fantasy'),
        ('biography', 'Biography'),
        ('poetry', 'Poetry'),
    ], string='Genre')
    rating = fields.Float(string='Rating', compute='_compute_rating', store=True)
    review_ids = fields.One2many('book.club.review', 'book_id', string='Reviews')

    @api.depends('review_ids.rating')
    def _compute_rating(self):
        for book in self:
            ratings = book.review_ids.mapped('rating')
            book.rating = sum(ratings) / len(ratings) if ratings else 0.0