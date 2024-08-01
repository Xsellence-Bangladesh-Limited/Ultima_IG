from odoo import http
from odoo.http import request as req


class AMCService(http.Controller):
    @http.route('/amc-service', type='http', auth='public')
    def amc_service(self):
        # Retrieving amc banner slider images (start)
        amc_banner_slider_images = req.env['ultima.amc.service.banner.slider'].sudo().search([], order='id asc')
        # Retrieving amc banner slider images (end)

        # Retrieving amc plans (start)
        amc_plans = req.env['ultima.amc.service.plan'].sudo().search([], order='id asc')
        # Retrieving amc plans (end)

        # Retrieving advantages (start)
        amc_advantages = req.env['ultima.amc.service.advantage'].sudo().search([], order='id asc')
        # Retrieving advantages (end)

        # Retrieving features (start)
        amc_features = req.env['ultima.amc.service.feature'].sudo().search([], order='id asc')
        # Retrieving features (end)

        # Retrieving testimonial slides (start)
        amc_testimonial_slides = req.env['ultima.amc.service.testimonial.slider'].sudo().search([], order='id asc')
        # Retrieving testimonial slides (end)

        # Retrieving amc page settings (start)
        amc_page_settings = req.env['ultima.amc.service.settings'].sudo().search([], order='id desc', limit=1)
        # Retrieving amc page settings (end)

        return req.render('ultima.ultima_amc_service_template', {
            'amc_banner_slider_images': amc_banner_slider_images,
            'amc_plans': amc_plans,
            'amc_advantages': amc_advantages,
            'amc_features': amc_features,
            'amc_testimonial_slides': amc_testimonial_slides,
            'amc_page_settings': amc_page_settings
        })
