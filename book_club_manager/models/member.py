from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class BookClubMember(models.Model):
    _name = 'book.club.member'
    _description = 'Book Club Member'


    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    full_name = fields.Char(string='Full Name', compute='_compute_full_name', store=True)
    age = fields.Integer(string='Age')
    join_date = fields.Date(string='Join Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    is_active = fields.Boolean(string='Is Active', default=True)
    notes = fields.Text(string='Notes')
    membership_type = fields.Selection([
        ('basic', 'Basic'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ], string='Membership type')

    member_ids = fields.Many2many('book.club.event', string='Events Attending')

    

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name or ''} {rec.last_name or ''}".strip()

    @api.onchange('age')
    def _onchange_age(self):
        if self.age and self.age < 12:
            return {
                'warning': {
                    'title': 'Too Young',
                    'message': 'Age under 12 years old.',
                }
            }
    @api.constrains('join_date')
    def _check_join_date(self):
        for rec in self:
            if rec.join_date and rec.join_date > date.today():
                raise ValidationError("Join date cannot be in the future.")