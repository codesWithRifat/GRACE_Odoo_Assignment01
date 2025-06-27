from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Many2one('res.partner', string='Name')
    class_id = fields.Char(string="Class")
    division = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C')], string="Division")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    birth_date = fields.Date(string="Birth Date")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    is_active = fields.Boolean(string="Active")
    profile_picture = fields.Binary(string="Profile Picture")
    notes = fields.Text(string="Notes")