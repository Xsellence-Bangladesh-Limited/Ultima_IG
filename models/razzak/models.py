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

    footer_desc = fields.Char(translate=True)
    # social_ids = fields.Many2many()
    note = fields.Char(translate=True)
    address = fields.Char(translate=True)
    contact_no = fields.Char(translate=True)
    whatsapp = fields.Char(translate=True)
    email = fields.Char()

    map_1920 = fields.Image("Map", max_width=1920, max_height=1920, required=True)
    map_1024 = fields.Image("Image 1024", related="map_1920", max_width=1024, max_height=1024, store=True)
    map_512 = fields.Image("Image 512", related="map_1920", max_width=512, max_height=512, store=True)
    map_256 = fields.Image("Image 256", related="map_1920", max_width=256, max_height=256, store=True)
    map_128 = fields.Image("Image 128", related="map_1920", max_width=128, max_height=128, store=True)
    map_url = fields.Char()

    quick_link_ids = fields.Many2many('ultima.quick_link')
    social_ids = fields.Many2many('ultima.social')

    tm_section = fields.Char(string='Section', required=True, translate=True)
    tm_title = fields.Char(string='Title', required=True, translate=True)


class UltimaQuick_link(models.Model):
    _name = 'ultima.quick_link'
    _description = 'ultima.quick_link'
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char(translate=True)
    url = fields.Char()


class UltimaSocial(models.Model):
    _name = 'ultima.social'
    _description = 'ultima.social'
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char(translate=True)
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

    section = fields.Char(translate=True)
    title = fields.Char(translate=True)
    desc = fields.Text(translate=True)
    desc_line_ids = fields.Many2many('ultima.home.introduce.desc.line')
    shop_now_url = fields.Char()
    shop_now_text = fields.Char()
    video_bg_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    video_bg_1024 = fields.Image("Image 1024", related="video_bg_1920", max_width=1024, max_height=1024, store=True)
    video_bg_512 = fields.Image("Image 512", related="video_bg_1920", max_width=512, max_height=512, store=True)
    video_bg_256 = fields.Image("Image 256", related="video_bg_1920", max_width=256, max_height=256, store=True)
    video_bg_128 = fields.Image("Image 128", related="video_bg_1920", max_width=128, max_height=128, store=True)

    video_url = fields.Char()


class UltimaHomeIntroduceDescLine(models.Model):
    _name = 'ultima.home.introduce.desc.line'
    _description = 'ultima.home.introduce.desc.line'
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char(required=True, translate=True)


class UltimaHome(models.Model):
    _name = 'ultima.home'
    _description = 'ultima.home'

    bsp_section = fields.Char(translate=True)
    bsp_title = fields.Char(translate=True)
    bsp_desc = fields.Text(translate=True)
    bsp_btn_text = fields.Char(translate=True)
    bsp_ids = fields.Many2many('product.template')

    dis_section = fields.Char(translate=True)
    dis_title = fields.Char(translate=True)
    dis_desc = fields.Char(translate=True)
    dis_line_ids = fields.Many2many('ultima.home.dis.line')

    type_section = fields.Char(translate=True)
    type_title = fields.Char(translate=True)
    type_ids = fields.Many2many('ultima.home.type.line')

    com_section = fields.Char(translate=True)
    com_title = fields.Char(translate=True)
    com_ids = fields.Many2many('ultima.home.com.line')

    client_title = fields.Char(translate=True)

    client_img_1920 = fields.Image("Client Images", max_width=1920, max_height=1920)
    client_img_1024 = fields.Image("Image 1024", related="client_img_1920", max_width=1024, max_height=1024, store=True)
    client_img_512 = fields.Image("Image 512", related="client_img_1920", max_width=512, max_height=512, store=True)
    client_img_256 = fields.Image("Image 256", related="client_img_1920", max_width=256, max_height=256, store=True)
    client_img_128 = fields.Image("Image 128", related="client_img_1920", max_width=128, max_height=128, store=True)

    faq_section = fields.Char(translate=True)
    faq_title = fields.Char(translate=True)
    faq_ids = fields.Many2many('ultima.home.faq')


class UltimaHomeDisLine(models.Model):
    _name = 'ultima.home.dis.line'
    _description = 'ultima.home.dis.line'
    _order = 'sequence'

    sequence = fields.Integer()

    img_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    img_1024 = fields.Image("Image 1024", related="img_1920", max_width=1024, max_height=1024, store=True)
    img_512 = fields.Image("Image 512", related="img_1920", max_width=512, max_height=512, store=True)
    img_256 = fields.Image("Image 256", related="img_1920", max_width=256, max_height=256, store=True)
    img_128 = fields.Image("Image 128", related="img_1920", max_width=128, max_height=128, store=True)
    title = fields.Char(translate=True)
    desc = fields.Text(translate=True)


class UltimaHomeTypeLine(models.Model):
    _name = 'ultima.home.type.line'
    _description = 'ultima.home.type.line'
    _order = 'sequence'

    sequence = fields.Integer()

    img_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    img_1024 = fields.Image("Image 1024", related="img_1920", max_width=1024, max_height=1024, store=True)
    img_512 = fields.Image("Image 512", related="img_1920", max_width=512, max_height=512, store=True)
    img_256 = fields.Image("Image 256", related="img_1920", max_width=256, max_height=256, store=True)
    img_128 = fields.Image("Image 128", related="img_1920", max_width=128, max_height=128, store=True)
    title = fields.Char(translate=True)
    button_text = fields.Char(translate=True)
    button_url = fields.Char(translate=True)
    line_ids = fields.Many2many('ultima.home.type.line.line')
    style = fields.Selection([
        ('left_img_right_text', 'Left Image And Right Text'),
        ('right_img_left_text', 'Right Image And Left Text'),
    ])


class UltimaHomeTypeLineLine(models.Model):
    _name = 'ultima.home.type.line.line'
    _description = 'ultima.home.type.line.line'
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char(translate=True)


class UltimaHomeComLine(models.Model):
    _name = 'ultima.home.com.line'
    _description = 'ultima.home.com.line'
    _order = 'sequence'

    sequence = fields.Integer()

    title = fields.Char(translate=True)
    desc = fields.Text(translate=True)
    img = fields.Char()
    ultima = fields.Boolean()


class UltimaHomeFaq(models.Model):
    _name = 'ultima.home.faq'
    _description = 'ultima.home.faq'
    _order = 'sequence'

    sequence = fields.Integer()
    title = fields.Char(translate=True)
    desc = fields.Text(translate=True)


class ProTemInherit(models.Model):
    _inherit = 'product.template'

    old_list_price = fields.Float()
    ribbon_id = fields.Many2one('ultima.ribbon')
    tag_ids = fields.Many2many('ultima.tag')
    website_publish = fields.Boolean()

    # Product Details
    short_desc = fields.Text()
    desc_line_ids = fields.Many2many('product.desc_line')

    p_detail_title = fields.Char()
    p_detail_desc = fields.Text()

    p_detail_hl_lbl = fields.Char()
    p_detail_desc_lbl = fields.Char()
    p_detail_spe_lbl = fields.Char()
    p_detail_hl_line_ids = fields.Many2many('product.p_detail_hl_line')

    p_detail_desc_line_ids = fields.Many2many('p_detail.desc_line')
    spe_line_ids = fields.Many2many('product.spe_line')


    """
    short_desc
    desc_line_ids
    
    p_detail_title
    p_detail_desc
    
    p_detail_hl_lbl
    p_detail_desc_lbl
    p_detail_spe_lbl
    p_detail_line_ids
    """


class ProductDesc_line(models.Model):
    _name = 'product.desc_line'
    _description = 'product.desc_line'

    name = fields.Char(required=True)


class ProductP_detail_hl_line(models.Model):
    _name = 'product.p_detail_hl_line'
    _description = 'product.p_detail_hl_line'

    name = fields.Char(required=True)
    # desc = fields.Char()
    line_ids = fields.Many2many('product.p_detail_hl_line2')


class ProductP_detail_hl_line2(models.Model):
    _name = 'product.p_detail_hl_line2'
    _description = 'product.p_detail_hl_line2'

    name = fields.Char(required=True)


class UltimaRibbon(models.Model):
    _name = 'ultima.ribbon'
    _description = 'ultima.ribbon'
    _rec_name = 'text'

    text = fields.Char(translate=True)
    bg_color = fields.Char()
    text_color = fields.Char()


class UltimaTag(models.Model):
    _name = 'ultima.tag'
    _description = 'ultima.tag'

    name = fields.Char(translate=True)
    bg_color = fields.Char()
    text_color = fields.Char()


class UltimaTestimonial(models.Model):
    _name = 'ultima.testimonial'
    _description = 'ultima.testimonial'
    _order = 'sequence'

    sequence = fields.Integer()

    section = fields.Char(translate=True)
    title = fields.Char(translate=True)
    desc = fields.Text(translate=True)
    person_name = fields.Char(translate=True)
    designation = fields.Char(translate=True)
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)


class UltimaProducts(models.Model):
    _name = 'ultima.products'
    _description = 'ultima.products'

    carousel_ids = fields.Many2many('ultima.products.carousel')

    oap_title = fields.Char(translate=True)
    oap_desc = fields.Char(translate=True)

    oaf_section = fields.Char(translate=True)
    oaf_title = fields.Char(translate=True)
    oaf_desc = fields.Char(translate=True)
    oaf_ids = fields.Many2many('ultima.products.feature')

    faq_section = fields.Char(translate=True)
    faq_title = fields.Char(translate=True)
    faq_ids = fields.Many2many('ultima.products.faq')


class UltimaProductsCarousel(models.Model):
    _name = 'ultima.products.carousel'
    _description = 'ultima.products.carousel'
    _order = 'sequence'

    sequence = fields.Integer()

    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)
    alt = fields.Char(translate=True)


class UltimaProductsFeature(models.Model):
    _name = 'ultima.products.feature'
    _description = 'ultima.products.feature'
    _order = 'sequence'

    sequence = fields.Integer()

    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)
    title = fields.Char(translate=True)
    desc = fields.Text(translate=True)


class UltimaProductsFaq(models.Model):
    _name = 'ultima.products.faq'
    _description = 'ultima.products.faq'
    _order = 'sequence'

    sequence = fields.Integer()

    title = fields.Char(translate=True)
    desc = fields.Text(translate=True)


class UltimaPd_detail(models.Model):
    _name = 'ultima.pd_detail'
    _description = 'ultima.pd_detail'

    faq_section = fields.Char(translate=True)
    faq_title = fields.Text(translate=True)
    faq_ids = fields.Many2many('ultima.pd_detail.faq')


class UltimaPd_detailFaq(models.Model):
    _name = 'ultima.pd_detail.faq'
    _description = 'ultima.pd_detail.faq'
    _order = 'sequence'

    sequence = fields.Integer()
    title = fields.Char(required=True, translate=True)
    desc = fields.Text(required=True, translate=True)


class UltimaWebsite_menu(models.Model):
    _name = 'ultima.website_menu'
    _description = 'ultima.website_menu'
    _rec_name = 'name'
    _order = 'sequence'

    sequence = fields.Integer()
    name = fields.Char()
    url = fields.Char()
    parent_id = fields.Many2one('ultima.website_menu')
    icon_class = fields.Char()
    new_window = fields.Boolean()


# class Def(models.Model):
#     _name = 'ultima.def'
#     _description = 'ultima.def'
#
#     name = fields.Char(string='Name')
#
#     def get_menus(self):
#         menus = self.env['ultima.website_menu'].sudo().search([])
#         print('menus', menus)

class P_detailDesc_line(models.Model):
    _name = 'p_detail.desc_line'
    _description = 'p_detail.desc_line'

    sequence = fields.Integer()

    img_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    img_1024 = fields.Image("Image 1024", related="img_1920", max_width=1024, max_height=1024, store=True)
    img_512 = fields.Image("Image 512", related="img_1920", max_width=512, max_height=512, store=True)
    img_256 = fields.Image("Image 256", related="img_1920", max_width=256, max_height=256, store=True)
    img_128 = fields.Image("Image 128", related="img_1920", max_width=128, max_height=128, store=True)

    title = fields.Char(translate=True)
    button_text = fields.Char(translate=True)
    desc = fields.Text(translate=True)
    style = fields.Selection([
        ('left_img_right_text', 'Left Image And Right Text'),
        ('right_img_left_text', 'Right Image And Left Text'),
    ])


class ProductSpe_line(models.Model):
    _name = 'product.spe_line'
    _description = 'product.spe_line'

    name = fields.Char(required=True, translate=True)
    value = fields.Char(required=True, translate=True)
