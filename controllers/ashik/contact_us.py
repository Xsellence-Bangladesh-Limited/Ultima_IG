from odoo import http
from odoo.http import request as req
from werkzeug.utils import redirect

class ContactUs(http.Controller):
    @http.route('/contact-us', type='http', auth='public')
    def contact_us(self):

        # Retrieving the page settings (start)
        page_settings = req.env['ultima.contact.us.page.settings'].sudo().search([], order='id desc', limit=1)
        # Retrieving the page settings (end)

        # Retrieving contact ways (start)
        contact_ways = req.env['ultima.contact.way'].sudo().search([], order='id asc')
        # Retrieving contact ways (end)

        # Retrieving default country data (start)
        all_default_countries = req.env['res.country'].sudo().search([])
        # Retrieving default country data (end)

        message_sent_successful = req.session.get('message_sent_successful')

        req.session['message_sent_successful'] = False

        return req.render('ultima.ultima_contact_us_template', {
            'contact_ways': contact_ways,
            'page_settings': page_settings,
            'all_default_countries': all_default_countries,
            'message_sent_successful': message_sent_successful
        })

    @http.route('/users-contact', type='http', auth='public', csrf=False)
    def users_contact(self, **form_data):
        if req.httprequest.method == 'POST':
            # Retrieving form data (start)
            first_name = form_data.get('first_name_input').strip() if form_data.get('first_name_input') else ''
            last_name = form_data.get('last_name_input').strip() if form_data.get('last_name_input') else ''
            email = form_data.get('email_input').strip() if form_data.get('email_input') else ''
            phone_number = form_data.get('phone_number_input').strip() if form_data.get('phone_number_input') else ''
            message = form_data.get('message_input').strip() if form_data.get('message_input') else ''
            # Retrieving form data(end)

            # Creating a new record in the ultima.users.message table (start)
            req.env['ultima.users.message'].sudo().create({
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number,
                'message': message
            })

            # Creating a new record in the ultima.users.message table (end)

            req.session['message_sent_successful'] = True
            return redirect('/contact-us')
