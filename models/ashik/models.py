from odoo import fields, models, api


# Models for contact us page (start)
class ContactWay(models.Model):
    _name = 'ultima.contact.way'
    _description = 'ultima.contact.way'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    title = fields.Char(string='Title')
    sub_title = fields.Char(string='Sub-title')
    contact_details = fields.Char(string='Contact details')
    contact_way_icon = fields.Image(string='Icon')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.contact.way.seq')
        return super(ContactWay, self).create(vals)


class UsersMessage(models.Model):
    _name = 'ultima.users.message'
    _description = 'ultima.users.message'
    _order = 'id desc'

    name = fields.Char(string='Sequence')

    first_name = fields.Char(string='First name')
    last_name = fields.Char(string='Last name')

    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone number')

    message = fields.Text(string='Message')

    date = fields.Datetime(default=lambda self: fields.Datetime.now(), string='Date')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.user.message.seq')
        return super(UsersMessage, self).create(vals)


class ContactUsPageSettings(models.Model):
    _name = 'ultima.contact.us.page.settings'
    _description = 'ultima.contact.us.page.settings'
    _order = 'id desc'

    name = fields.Char(string='Name')
    form_illustration = fields.Image(string='Form illustration')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.contact.us.settings.seq')
        return super(ContactUsPageSettings, self).create(vals)

# Models for contact us page (end)

# Models for AMC service page (start)

class AMCServiceBannerSlider(models.Model):
    _name = 'ultima.amc.service.banner.slider'
    _description = 'ultima.amc.service.banner.slider'
    _order = 'id desc'

    name = fields.Char(string='Name')
    slider_image = fields.Image(string='Slider image')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.banner.slider.seq')
        return super(AMCServiceBannerSlider, self).create(vals)


class AMCServiceTestimonialSlider(models.Model):
    _name = 'ultima.amc.service.testimonial.slider'
    _description = 'ultima.amc.service.testimonial.slider'
    _order = 'id desc'

    name = fields.Char('Name')
    client_image = fields.Image(string='Client image')
    client_comment = fields.Text(string='Client comment')
    client_name = fields.Char(string='Client name')
    client_designation = fields.Char(string='Client designation')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.testimonial.slider.seq')
        return super(AMCServiceTestimonialSlider, self).create(vals)

# Models for AMC service page (end)

# Models for service request page (start)

class ServiceRequestTestimonialSlide(models.Model):
    _name = 'ultima.service.request.testimonial.slider'
    _description = 'ultima.service.request.testimonial.slider'
    _order = 'id desc'

    name = fields.Char('Name')
    client_image = fields.Image(string='Client image')
    client_comment = fields.Text(string='Client comment')
    client_name = fields.Char(string='Client name')
    client_designation = fields.Char(string='Client designation')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.service.request.testimonial.slider.seq')
        return super(ServiceRequestTestimonialSlide, self).create(vals)

# Models for service request page (end)


