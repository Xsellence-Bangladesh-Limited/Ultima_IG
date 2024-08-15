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


class UltimaHomeIntroduce(models.Model):
    _name = 'ultima.home.introduce'
    _description = 'ultima.home.introduce'

    section = fields.Char()
    title = fields.Char()
    desc = fields.Text()
    desc_line_ids = fields.Many2many('ultima.home.introduce.desc.line')
    shop_now_url = fields.Char()
    video_bg_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    video_bg_1024 = fields.Image("Image 1024", related="video_bg_1920", max_width=1024, max_height=1024, store=True)
    video_bg_512 = fields.Image("Image 512", related="video_bg_1920", max_width=512, max_height=512, store=True)
    video_bg_256 = fields.Image("Image 256", related="video_bg_1920", max_width=256, max_height=256, store=True)
    video_bg_128 = fields.Image("Image 128", related="video_bg_1920", max_width=128, max_height=128, store=True)

    video_url = fields.Char()


class UltimaHomeIntroduceDescLine(models.Model):
    _name = 'ultima.home.introduce.desc.line'
    _description = 'ultima.home.introduce.desc.line'

    name = fields.Char(required=True)


class UltimaHome(models.Model):
    _name = 'ultima.home'
    _description = 'ultima.home'

    bsp_section = fields.Char()
    bsp_title = fields.Char()
    bsp_desc = fields.Text()

    dis_section = fields.Char()
    dis_title = fields.Char()
    dis_desc = fields.Char()
    dis_line_ids = fields.Many2many('ultima.home.dis.line')

    type_section = fields.Char()
    type_title = fields.Char()
    type_ids = fields.Many2many('ultima.home.type.line')

    com_section = fields.Char()
    com_title = fields.Char()
    com_ids = fields.Many2many('ultima.home.com.line')

    client_title = fields.Char()

    client_img_1920 = fields.Image("Client Images", max_width=1920, max_height=1920)
    client_img_1024 = fields.Image("Image 1024", related="client_img_1920", max_width=1024, max_height=1024, store=True)
    client_img_512 = fields.Image("Image 512", related="client_img_1920", max_width=512, max_height=512, store=True)
    client_img_256 = fields.Image("Image 256", related="client_img_1920", max_width=256, max_height=256, store=True)
    client_img_128 = fields.Image("Image 128", related="client_img_1920", max_width=128, max_height=128, store=True)

    faq_section = fields.Char()
    faq_title = fields.Char()
    faq_ids = fields.Many2many('ultima.home.faq')


class UltimaHomeDisLine(models.Model):
    _name = 'ultima.home.dis.line'
    _description = 'ultima.home.dis.line'

    img_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    img_1024 = fields.Image("Image 1024", related="img_1920", max_width=1024, max_height=1024, store=True)
    img_512 = fields.Image("Image 512", related="img_1920", max_width=512, max_height=512, store=True)
    img_256 = fields.Image("Image 256", related="img_1920", max_width=256, max_height=256, store=True)
    img_128 = fields.Image("Image 128", related="img_1920", max_width=128, max_height=128, store=True)
    title = fields.Char()
    desc = fields.Text()


class UltimaHomeTypeLine(models.Model):
    _name = 'ultima.home.type.line'
    _description = 'ultima.home.type.line'

    img_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    img_1024 = fields.Image("Image 1024", related="img_1920", max_width=1024, max_height=1024, store=True)
    img_512 = fields.Image("Image 512", related="img_1920", max_width=512, max_height=512, store=True)
    img_256 = fields.Image("Image 256", related="img_1920", max_width=256, max_height=256, store=True)
    img_128 = fields.Image("Image 128", related="img_1920", max_width=128, max_height=128, store=True)
    title = fields.Char()
    button_text = fields.Char()
    button_url = fields.Char()
    line_ids = fields.Many2many('ultima.home.type.line.line')
    style = fields.Selection([
        ('left_img_right_text', 'Left Image And Right Text'),
        ('right_img_left_text', 'Right Image And Left Text'),
    ])


class UltimaHomeTypeLineLine(models.Model):
    _name = 'ultima.home.type.line.line'
    _description = 'ultima.home.type.line.line'

    name = fields.Char()


class UltimaHomeComLine(models.Model):
    _name = 'ultima.home.com.line'
    _description = 'ultima.home.com.line'

    title = fields.Char()
    desc = fields.Text()
    img = fields.Char()
    sequence = fields.Integer()
    ultima = fields.Boolean()


class UltimaHomeFaq(models.Model):
    _name = 'ultima.home.faq'
    _description = 'ultima.home.faq'

    title = fields.Char()
    desc = fields.Text()


class ProTemInherut(models.Model):
    _inherit = 'product.template'

    old_list_price = fields.Float()
    ribbon_id = fields.Many2one('ultima.ribbon')
    tag_ids = fields.Many2many('ultima.tag')


class UltimaRibbon(models.Model):
    _name = 'ultima.ribbon'
    _description = 'ultima.ribbon'
    _rec_name = 'text'

    text = fields.Char()
    bg_color = fields.Char()
    text_color = fields.Char()


class UltimaTag(models.Model):
    _name = 'ultima.tag'
    _description = 'ultima.tag'

    name = fields.Char()
    bg_color = fields.Char()
    text_color = fields.Char()


class UltimaTestimonial(models.Model):
    _name = 'ultima.testimonial'
    _description = 'ultima.testimonial'

    section = fields.Char()
    title = fields.Char()
    desc = fields.Text()
    person_name = fields.Char()
    designation = fields.Char()
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)
