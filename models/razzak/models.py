from odoo import fields, models, api


class UltimaLayout(models.Model):
    _name = 'ultima.layout'
    _description = 'ultima.layout'

    logo_1920 = fields.Image("Logo", max_width=1920, max_height=1920, required=True)
    logo_1024 = fields.Image("Image 1024", related="logo_1920", max_width=1024, max_height=1024, store=True)
    logo_512 = fields.Image("Image 512", related="logo_1920", max_width=512, max_height=512, store=True)
    logo_256 = fields.Image("Image 256", related="logo_1920", max_width=256, max_height=256, store=True)
    logo_128 = fields.Image("Image 128", related="logo_1920", max_width=128, max_height=128, store=True)

    footer_logo_1920 = fields.Image("Footer Logo", max_width=1920, max_height=1920, required=True)
    footer_logo_1024 = fields.Image("Image 1024", related="footer_logo_1920", max_width=1024, max_height=1024,
                                    store=True)
    footer_logo_512 = fields.Image("Image 512", related="footer_logo_1920", max_width=512, max_height=512, store=True)
    footer_logo_256 = fields.Image("Image 256", related="footer_logo_1920", max_width=256, max_height=256, store=True)
    footer_logo_128 = fields.Image("Image 128", related="footer_logo_1920", max_width=128, max_height=128, store=True)

    footer_desc = fields.Char()
    # social_ids = fields.Many2many()
    note = fields.Char()
    address = fields.Char()
    contact_no = fields.Char()
    whatsapp = fields.Char()
    email = fields.Char()

    map_1920 = fields.Image("Map", max_width=1920, max_height=1920, required=True)
    map_1024 = fields.Image("Image 1024", related="map_1920", max_width=1024, max_height=1024, store=True)
    map_512 = fields.Image("Image 512", related="map_1920", max_width=512, max_height=512, store=True)
    map_256 = fields.Image("Image 256", related="map_1920", max_width=256, max_height=256, store=True)
    map_128 = fields.Image("Image 128", related="map_1920", max_width=128, max_height=128, store=True)
    map_url = fields.Char()

    quick_link_ids = fields.Many2many('ultima.quick_link')
    social_ids = fields.Many2many('ultima.social')


class UltimaQuick_link(models.Model):
    _name = 'ultima.quick_link'
    _description = 'ultima.quick_link'

    name = fields.Char()
    url = fields.Char()


class UltimaSocial(models.Model):
    _name = 'ultima.social'
    _description = 'ultima.social'

    name = fields.Char()
    logo_1920 = fields.Image("Logo", max_width=1920, max_height=1920)
    logo_1024 = fields.Image("Image 1024", related="logo_1920", max_width=1024, max_height=1024, store=True)
    logo_512 = fields.Image("Image 512", related="logo_1920", max_width=512, max_height=512, store=True)
    logo_256 = fields.Image("Image 256", related="logo_1920", max_width=256, max_height=256, store=True)
    logo_128 = fields.Image("Image 128", related="logo_1920", max_width=128, max_height=128, store=True)

    svg = fields.Char()
    url = fields.Char()
