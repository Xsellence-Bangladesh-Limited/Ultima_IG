from odoo import fields, models, api

class Test(models.Model):
    _name = 'ultima.ig.test'
    _description = 'ultima.ig.test'

    name = fields.Char()