from odoo import models, fields

class BookClubReview(models.Model):
    _name = 'book.club.review'
    _description = 'Book Review'

    full_name = fields.Many2one('book.club.member', string='Reviewer', required=True)
    book_id = fields.Many2one('book.club.book', string='Book', required=True)
    review_date = fields.Date(string='Review Date')
    rating = fields.Integer(string='Rating', default=0)
    comments = fields.Text(string='Comments')
