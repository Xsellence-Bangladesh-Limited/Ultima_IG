from odoo import fields, models, api

class TestRaz(models.Model):
    _name = 'ultima.ig.test.raz'
    _description = 'ultima.ig.test.raz'

    name = fields.Char()
    age = fields.Integer()