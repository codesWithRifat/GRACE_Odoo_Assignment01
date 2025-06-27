from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_book = fields.Boolean(string='Is a Book')
    book_genre = fields.Selection([
        ('islamic', 'Islamic'),
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('biography', 'Biography'),
        ('fantasy', 'Fantasy'),
        ('poetry', 'Poetry'),
    ], string='Book Genre', help='Select if this product is a book')

    author_name = fields.Char(string='Author')
    publish_date = fields.Date(string='Publish Date')

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_book_club_order = fields.Boolean(string='Book Club Order')
    membership_level = fields.Selection([
        ('basic', 'Basic'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ], string='Membership Level')