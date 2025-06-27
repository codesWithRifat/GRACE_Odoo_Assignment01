from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class BookClubEvent(models.Model):
    _name = 'book.club.event'
    _description = 'Book Club Event'

    name = fields.Char(string='Event Name', required=True)
    event_date = fields.Datetime(string='Event Date', required=True)

    location = fields.Char(string='Location')
    description = fields.Text(string='Description')
    member_ids = fields.Many2many('book.club.member', string='Participants')
    @api.constrains('event_date')
    def _check_event_date_not_past(self):
        for rec in self:
            if rec.event_date and rec.event_date < fields.Datetime.now():
                raise ValidationError("You cannot schedule an event in the past.")