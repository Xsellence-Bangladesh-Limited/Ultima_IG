from odoo import fields, models, api
from datetime import datetime
from odoo.exceptions import ValidationError, UserError
from odoo.http import request as req
from odoo.exceptions import ValidationError
import requests

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
    main_headline = fields.Char(string='Main headline', translate=True)
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


class AMCServiceFAQ(models.Model):
    _name = 'ultima.amc.service.faq'
    _description = 'ultima.amc.service.faq'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    title = fields.Char(string='Title')
    description = fields.Text(string='Description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.amc.service.faq.seq')
        return super(AMCServiceFAQ, self).create(vals)

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


class UltimaServiceRequest(models.Model):
    _name = 'ultima.service.request'
    _description = 'ultima.service.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name')
    full_name = fields.Char(string='Customer Name', required=True)
    registered_mobile_number = fields.Char(string='Customer Mobile Number', required=True)
    customer_address = fields.Text("Customer Address", tracking=True)
    planned_date_begin = fields.Datetime("Planned Date Begin", required=True)
    date_deadline = fields.Datetime("Deadline", required=True)
    partner_id = fields.Many2one('res.partner', "Existing Partner", compute='_compute_partner')
    task_id = fields.Many2one("project.task", "Task", readonly=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('approve', 'Approved')], readonly=True,
        default='draft', copy=False, string="Status", tracking=True)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.service.request.seq')
        return super(UltimaServiceRequest, self).create(vals)

    @api.depends('registered_mobile_number')
    def _compute_partner(self):
        for rec in self:
            mobile_code = ''
            rec.partner_id = False

            if rec.registered_mobile_number:
                if rec.registered_mobile_number.startswith("01"):
                    mobile_code = '+88'

                elif rec.registered_mobile_number.startswith("1"):
                    mobile_code = '+880'
                rec.registered_mobile_number = mobile_code + rec.registered_mobile_number
                ext_customer = self.env['res.partner'].search([('mobile', '=', rec.registered_mobile_number)])
                if ext_customer:
                    if len(ext_customer) == 1:
                        rec.partner_id = ext_customer.id
                    else:
                        raise ValidationError("Multiple Partners are already created with this mobile Number.")

    def action_approve(self):
        for rec in self:
            # Create Customer Record

            customer = self.env['res.partner'].search([('mobile', '=', rec.registered_mobile_number)])
            if not customer:
                customer_env = self.env['res.partner']
                customer = customer_env.create({
                    'name': rec.full_name,
                    'street': rec.customer_address,
                    'mobile': rec.registered_mobile_number,
                })

            # Create Task Record

            project = self.env['project.project'].search([('name', '=', 'Field Service')])
            task_env = self.env['project.task']
            new_task = task_env.create({
                'project_id': project.id,
                'name': rec.name + " - Service Request",
                'partner_id': customer.id,
                'planned_date_begin': rec.planned_date_begin,
                'date_deadline': rec.date_deadline,
                'service_request_id': rec.id,
                'user_ids': False,
            })
            print("new_task: ", new_task)

            rec.task_id = new_task.id
            rec.state = 'approve'


class ProjectTask(models.Model):
    _inherit = "project.task"

    service_request_id = fields.Many2one("ultima.service.request", "Service Request No", tracking=True)


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


class UltimaServiceRequestFAQ(models.Model):
    _name = 'ultima.service.request.faq'
    _description = 'ultima.service.request.faq'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    title = fields.Char(string='Title')
    description = fields.Text(string='Description')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.service.request.faq.seq')
        return super(UltimaServiceRequestFAQ, self).create(vals)


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


class AboutUsGrowthData(models.Model):
    _name = 'ultima.about.us.growth.data'
    _description = 'ultima.about.us.growth.data'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    number = fields.Char(string='Number')
    title = fields.Char(string='Title')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.about.us.growth.data.seq')
        return super(AboutUsGrowthData, self).create(vals)

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


class AboutUsSettings(models.Model):
    _name = 'ultima.about.us.settings'
    _description = 'ultima.about.us.settings'
    _order = 'id desc'

    name = fields.Char(string='Name')
    introduction_image = fields.Image(string='Introduction image')
    introduction_title = fields.Char(string='Introduction title')
    introduction_description = fields.Text(string='Introduction description')

    client_title_part_1 = fields.Char(string='Clients title part 1')
    number_of_clients = fields.Char(string='Number of clients')
    client_title_part_2 = fields.Char(string='Clients title part 2')

    feature_title = fields.Char(string='Features title')
    feature_short_description = fields.Text(string='Features short description')

    growth_title = fields.Char(string='Growth title')
    growth_short_description = fields.Text(string='Growth short description')

    offer_title = fields.Char(string='Offers title')
    offer_description = fields.Text(string='Offers description')
    offer_upper_image = fields.Image(string='Offers upper image')
    offer_lower_image = fields.Image(string='Offers lower image')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.about.us.settings.seq')
        return super(AboutUsSettings, self).create(vals)

# Models for about us page (end)

# Models for blog (start)

class BlogCategory(models.Model):
    _name = 'ultima.blog.category'
    _description = 'ultima.blog.category'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    category_name = fields.Char(string='Category name')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.blog.category.seq')
        return super(BlogCategory, self).create(vals)

class Blog(models.Model):
    _name = 'ultima.blog.blog'
    _description = 'ultima.blog.blog'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    banner_image = fields.Image(string='Banner image')
    title = fields.Char(string='Title')
    content = fields.Html(string='Content')
    category_id = fields.Many2one('ultima.blog.category', string='Category')
    estimated_time_to_read = fields.Char(string='Estimated time to read')
    publication_date = fields.Date(default=lambda self: fields.Date.today(), string='Publication date')
    author_id = fields.Many2one('res.users', string='Author')
    slug = fields.Char(string='Slug', compute='_compute_blog_slug')

    @api.depends('title')
    def _compute_blog_slug(self):
        for rec in self:
            title = str(rec.title)
            if '?' in title:
                title = title.replace('?', '')
            if '&' in title:
                title = title.replace('&', 'and')
            rec.slug = '-'.join(title.split(' ')) + '-' + str(datetime.now())

    def format_blog_date(self):
        date_obj = datetime.strptime(str(self.publication_date), "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")

        return formatted_date

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.blog.blog.seq')
        return super(Blog, self).create(vals)

class SuggestedBlog(models.Model):
    _name = 'ultima.suggested.blog'
    _description = 'ultima.suggested.blog'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    main_blog_id = fields.Many2one('ultima.blog.blog', string='Main blog')
    suggested_blog_ids = fields.Many2many('ultima.blog.blog', string='Suggested blogs')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.suggested.blog.seq')
        return super(SuggestedBlog, self).create(vals)

class BlogQuery(models.Model):
    _name = 'ultima.blog.query'
    _description = 'ultima.blog.query'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    user_name = fields.Char(string='Name')
    user_email = fields.Char(string='Email')
    user_mobile = fields.Char(string='Mobile')
    blog_id = fields.Many2one('ultima.blog.blog', string='Blog')
    date = fields.Datetime(string='Date', default=lambda self: fields.Datetime.now())

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.blog.query.seq')
        return super(BlogQuery, self).create(vals)


class BlogComment(models.Model):
    _name = 'ultima.blog.comment'
    _description = 'ultima.blog.comment'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    user_id = fields.Many2one('res.partner', string='User')
    comment = fields.Text(string='Comment')
    blog_id = fields.Many2one('ultima.blog.blog', string='Blog')
    date = fields.Datetime(string='Date', default=lambda self: fields.Datetime.now())

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.blog.comment.seq')
        return super(BlogComment, self).create(vals)

class BlogSlider(models.Model):
    _name = 'ultima.blog.slider'
    _description = 'ultima.blog.slider'
    _order = 'id desc'

    name = fields.Char(string='Sequence')
    blog_id = fields.Many2one('ultima.blog.blog', string='Blog')
    slider_description = fields.Text(string='Slider description')

    def format_blog_date(self):
        date_obj = datetime.strptime(str(self.creation_date), "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")

        return formatted_date

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.blog.slider.seq')
        return super(BlogSlider, self).create(vals)

# Models for blog (end)

class BlogSettings(models.Model):
    _name = 'ultima.blog.settings'
    _description = 'ultima.blog.settings'
    _order = 'id desc'

    name = fields.Char(string='Name')
    query_form_title = fields.Char(string='Query form title')
    query_form_button_text = fields.Char(string='Query form button text')
    query_submission_success_modal_title = fields.Char(string='Query submission success modal title')
    query_submission_success_modal_description = fields.Char(string='Query submission success modal description')
    query_submission_success_modal_button_text = fields.Char(string='Query submission success modal button text')
    comment_form_button_text = fields.Char(string='Comment form button text')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('ultima.blog.settings.seq')
        return super(BlogSettings, self).create(vals)


class UltimaAccountMoveInherit(models.Model):
    _inherit = 'account.move'

    is_posted = fields.Boolean(default=False)

    def action_register_payment(self):
        self.is_posted = True
        return super(UltimaAccountMoveInherit, self).action_register_payment()

    def send_sms(self):
        sms_settings = req.env['ultima.sms.settings'].sudo().search([], order='id desc', limit=1)

        if self.partner_id.phone:
            data = {
                'api_key': sms_settings.api_key if sms_settings.api_key else 'C200918366ebcc11bc0e03.88783932',
                'type': 'unicode',
                'contacts': f"880{self.partner_id.phone[-10:]}",
                'senderid': '8809601011978',
                'msg': f"""Dear sir/ma'am, A new invoice has been generated for you.
                        Invoice: {self.name}
                        invoice date: {self.invoice_date}
                        delivery date: {self.delivery_date}
                        Total amount: {self.amount_total} 
                        Due amount: {self.amount_residual}
                        Thanks for purchasing from Ultima Bangladesh LTD.
                """
            }

            try:

                r = requests.post(f"https://msg.elitbuzz-bd.com/smsapi", json=data)

                if r.status_code == 200:

                    self.is_posted = False

                    return {
                        'effect': {
                            'fadeout': 'slow',
                            'message': 'SMS has been sent successfully.',
                            'type': 'rainbow_man'
                        }
                    }
                else:
                    raise ValidationError("Something went wrong! Looks like the customer's phone number is not correct.")

            except Exception as e:
                raise ValidationError("Something went wrong! Looks like the customer's phone number is not correct.")

        else:
            raise ValidationError("Looks like the selected customer doesn't have any phone number.")