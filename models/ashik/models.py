from odoo import fields, models, api

class UsersMessage(models.Model):
    _name = 'ultima.users.message'
    _description = 'ultima.users.message'
    _rec_name = 'email'
    _order = 'id desc'

    first_name = fields.Char(string='First name')
    last_name = fields.Char(string='Last name')

    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone number')

    message = fields.Text(string='Message')

    date = fields.Datetime(default=lambda self: fields.Datetime.now(), string='Date')

class ContactUsPageSettings(models.Model):
    _name = 'ultima.contact.us.page.settings'
    _description = 'ultima.contact.us.page.settings'

    form_illustration = fields.Image(string='Form illustration')


