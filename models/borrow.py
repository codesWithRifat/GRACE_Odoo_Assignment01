from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Book Borrow'

    member_id = fields.Many2one('library.member', string='Member',  required=True)
    book_id = fields.Many2one( 'library.book', string='Book', required=True)
    borrow_date = fields.Date( string='Borrow Date', default=fields.Date.context_today,  required=True )
    return_date = fields.Date(string='Return Date')
    quantity = fields.Integer(string='Quantity', default=1,  required=True )

    @api.onchange('book_id', 'quantity')
    def _onchange_book_qty(self):
        if not self.book_id:
            return
        if self.quantity <= 0:
            raise ValidationError("Quantity must be at least 1")
        if self.quantity > self.book_id.numOfcopys:
            raise ValidationError(
                f"Only {self.book_id.numOfcopys} copies available, cannot borrow {self.quantity}."
            )
        self.book_id.numOfcopys = self.book_id.numOfcopys - self.quantity

    @api.onchange('return_date')
    def _onchange_return(self):
        if self.return_date:
            if self.return_date < self.borrow_date:
                raise ValidationError("Return date cannot be before borrow date.")
            self.book_id.numOfcopys = self.book_id.numOfcopys + self.quantity
