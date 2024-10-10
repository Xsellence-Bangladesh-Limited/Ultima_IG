from odoo import http
from odoo.http import request as req
from werkzeug.utils import redirect

class ServiceRequest(http.Controller):
    @http.route('/service-request', type='http', auth='public')
    def service_request(self):

        # Retrieving form points (start)
        form_points = req.env['ultima.service.request.form.point'].sudo().search([], order='id asc')
        # Retrieving form points (end)

        # Retrieving features (start)
        service_request_features = req.env['ultima.service.request.feature'].sudo().search([], order='id asc')
        # Retrieving features (end)

        # Retrieving amc faqs (start)
        service_request_faqs = req.env['ultima.service.request.faq'].sudo().search([], order='id desc')
        # Retrieving amc faqs (end)

        # Retrieving testimonial slides (start)
        service_request_testimonial_slides = req.env['ultima.service.request.testimonial.slider'].sudo().search([],
                                                                                                                order='id asc')
        # Retrieving testimonial slides (end)

        # Retrieving settings (start)
        service_request_settings = req.env['ultima.service.request.settings'].sudo().search([], order='id desc', limit=1)
        # Retrieving settings (end)

        request_sent_successful = req.session.get('request_sent_successful')

        req.session['request_sent_successful'] = False

        return req.render('ultima.ultima_service_request_template', {
            'form_points': form_points,
            'service_request_features': service_request_features,
            'service_request_faqs': service_request_faqs,
            'service_request_testimonial_slides': service_request_testimonial_slides,
            'service_request_settings': service_request_settings,
            'request_sent_successful': request_sent_successful
        })

    @http.route('/users-service-request', type='http', auth='public', csrf=False)
    def users_service_request(self, **form_data):
        if req.httprequest.method == 'POST':
            full_name = form_data.get('requester_name').strip() if form_data.get('requester_name') else ''
            address = form_data.get('requester_address').strip() if form_data.get('requester_address') else ''
            mobile_number = form_data.get('requester_mobile_number').strip() if form_data.get(
                'requester_mobile_number') else ''
            preferred_date = form_data.get('requester_preferred_date').strip() if form_data.get(
                'requester_preferred_date') else ''
            # preferred_time = form_data.get('requester_preferred_time').strip() if form_data.get(
            #     'requester_preferred_time') else ''

            # Creating a new record in the ultima.service.request table (start)
            req.env['ultima.service.request'].sudo().create({
                'full_name': full_name,
                'customer_address': address,
                'registered_mobile_number': mobile_number,
                'date_deadline': preferred_date,
            })
            # Creating a new record in the ultima.service.request table (end)

            req.session['request_sent_successful'] = True

            return redirect('/service-request')