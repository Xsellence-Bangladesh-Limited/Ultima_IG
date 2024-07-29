from odoo import http
from odoo.http import request as req

class ContactUs(http.Controller):
    @http.route('/contact-us', type='http', auth='public', csrf=False)
    def contact_us(self, **form_data):

        # Retrieving the page settings (start)
        page_settings = req.env['ultima.contact.us.page.settings'].sudo().search([], order='id desc', limit=1)
        # Retrieving the page settings (end)

        if req.httprequest.method == 'POST':

            # Retrieving form data (start)
            first_name = form_data.get('first_name_input')
            last_name = form_data.get('last_name_input')
            email = form_data.get('email_input')
            phone_number = form_data.get('phone_number_input')
            message = form_data.get('message_input')
            # Retrieving form data(end)

            # Creating a new record in the ultima.users.message table (start)
            req.env['ultima.users.message'].sudo().create({
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number,
                'message': message
            })

            return req.render('ultima.ultima_contact_us_template', {
                'message_sent_successful': True,
                'page_settings': page_settings
            })
            # Creating a new record in the ultima.users.message table (end)

        return req.render('ultima.ultima_contact_us_template', {
            'page_settings': page_settings
        })
