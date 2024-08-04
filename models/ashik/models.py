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
    main_headline = fields.Char(string='Main headline')
    main_sub_headline = fields.Char(string='Main sub-headline')
    form_headline = fields.Char(string='Form headline')
    form_sub_headline = fields.Char(string='Form sub-headline')
    form_illustration = fields.Image(string='Form image')

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


class AMCServicePlanFeature(models.Model):
    _name = 'ultima.amc.service.plan.feature'
    _description = 'ultima.amc.service.plan.feature'
    _order = 'id desc'

    name = fields.Char(string='Name')
    icon = fields.Image(string='Icon')
    short_description = fields.Text(string='Short description')

    @api.depends('name', 'short_description')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'{rec.short_description} ({rec.name})'

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.plan.feature.seq')
        return super(AMCServicePlanFeature, self).create(vals)


class AMCServicePlan(models.Model):
    _name = 'ultima.amc.service.plan'
    _description = 'ultima.amc.service.plan'
    _order = 'id desc'

    name = fields.Char(string='Name')
    icon = fields.Image(string='Icon')
    title = fields.Char(string='Title')
    plan_feature_ids = fields.Many2many('ultima.amc.service.plan.feature', string='Plan features')
    discount_icon = fields.Image(string='Discount icon')
    discount_description = fields.Char(string='Discount description')
    discount_type = fields.Selection([
        ('not_available', 'Not available'),
        ('free', 'Free'),
        ('percentage', 'Percentage')
    ], default='not_available')

    discount_percentage = fields.Integer(string='Discount percentage')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.plan.seq')
        return super(AMCServicePlan, self).create(vals)

class AMCServiceAdvantage(models.Model):
    _name = 'ultima.amc.service.advantage'
    _description = 'ultima.amc.service.advantage'
    _order = 'id desc'

    name = fields.Char('Name')
    icon = fields.Image('Icon')
    short_description = fields.Text('Short description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.advantage.seq')
        return super(AMCServiceAdvantage, self).create(vals)


class AMCServiceFeature(models.Model):
    _name = 'ultima.amc.service.feature'
    _description = 'ultima.amc.service.feature'
    _order = 'id desc'

    name = fields.Char('Name')
    icon = fields.Image('Icon')
    title = fields.Char('Title')
    short_description = fields.Text('Short description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.feature.seq')
        return super(AMCServiceFeature, self).create(vals)


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


class AMCServiceSettings(models.Model):
    _name = 'ultima.amc.service.settings'
    _description = 'ultima.amc.service.settings'
    _order = 'id desc'

    name = fields.Char(string='Name')

    plan_title = fields.Char(string='Plan title')
    plan_short_description = fields.Text(string='Plan short description')

    advantage_title = fields.Char(string='Advantage title')
    advantage_description = fields.Text(string='Advantage description')
    advantage_upper_image = fields.Image(string='Advantage upper image')
    advantage_lower_image = fields.Image(string='Advantage lower image')

    feature_title = fields.Char(string='Feature title')
    feature_short_description = fields.Text(string='Feature short description')

    testimonial_title = fields.Char(string='Testimonial title')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.settings.seq')
        return super(AMCServiceSettings, self).create(vals)

# Models for AMC service page (end)

# Models for service request page (start)

class UltimaServiceRequest(models.Model):
    _name = 'ultima.service.request'
    _description = 'ultima.service.request'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    full_name = fields.Char(string='Full name')
    registered_mobile_number = fields.Char(string='Registered mobile number')
    preferred_date = fields.Char(string='Preferred date')
    preferred_time = fields.Char(string='Preferred time')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.service.request.seq')
        return super(ServiceRequest, self).create(vals)

class ServiceRequestFormPoint(models.Model):
    _name = 'ultima.service.request.form.point'
    _description = 'ultima.service.request.form.point'
    _order = 'id desc'

    name = fields.Char(string='Name')
    title = fields.Char(string='Title')
    sub_title = fields.Char(string='Sub title')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.service.request.form.point.seq')
        return super(ServiceRequestFormPoint, self).create(vals)

class ServiceRequestFeature(models.Model):
    _name = 'ultima.service.request.feature'
    _description = 'ultima.service.request.feature'
    _order = 'id desc'

    name = fields.Char(string='Name')
    icon = fields.Image(string='Icon')
    title = fields.Char(string='Title')
    short_description = fields.Text(string='Short description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.service.request.feature.seq')
        return super(ServiceRequestFeature, self).create(vals)


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


class ServiceRequestSettings(models.Model):
    _name = 'ultima.service.request.settings'
    _description = 'ultima.service.request.settings'
    _order = 'id desc'

    name = fields.Char(string='Name')
    banner_image = fields.Image(string='Banner image')
    form_title = fields.Char(string='Form title')
    feature_title = fields.Char(string='Feature title')
    feature_short_description = fields.Text(string='Feature short description')
    testimonial_title = fields.Char(string='Testimonial title')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.service.request.settings')
        return super(ServiceRequestSettings, self).create(vals)

# Models for service request page (end)

# Models for about us page (start)

class AboutUsClient(models.Model):
    _name = 'ultima.about.us.client'
    _description = 'ultima.about.us.client'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    client_logo = fields.Image(string='Client logo')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.about.us.client.seq')
        return super(AboutUsClient, self).create(vals)

class AboutUsFeature(models.Model):
    _name = 'ultima.about.us.feature'
    _description = 'ultima.about.us.feature'
    _order = 'id desc'

    name = fields.Char(string='Name')
    icon = fields.Image(string='Icon')
    title = fields.Char(string='Title')
    short_description = fields.Text(string='Short description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.about.us.feature.seq')
        return super(AboutUsFeature, self).create(vals)


class AboutUsOffer(models.Model):
    _name = 'ultima.about.us.offer'
    _description = 'ultima.about.us.offer'
    _order = 'id desc'

    name = fields.Char('Name')
    icon = fields.Image('Icon')
    short_description = fields.Text('Short description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.about.us.offer.seq')
        return super(AboutUsOffer, self).create(vals)

# Models for about us page (end)


