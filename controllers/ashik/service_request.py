from odoo import http
from odoo.http import request as req


class ServiceRequest(http.Controller):
    @http.route('/service-request', type='http', auth='public')
    def service_request(self):
        # Retrieving testimonial slides (start)
        service_request_testimonial_slides = req.env['ultima.service.request.testimonial.slider'].sudo().search([], order='id asc')
        # Retrieving testimonial slides (end)

        return req.render('ultima.ultima_service_request_template', {
            'service_request_testimonial_slides': service_request_testimonial_slides
        })