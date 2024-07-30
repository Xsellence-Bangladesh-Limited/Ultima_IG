from odoo import http
from odoo.http import request as req

class AMCService(http.Controller):
    @http.route('/amc-service', type='http', auth='public')
    def amc_service(self):
        # Retrieving amc banner slider images (start)
        amc_banner_slider_images = req.env['ultima.amc.service.banner.slider'].sudo().search([], order='id asc')
        # Retrieving amc banner slider images (end)
        return req.render('ultima.ultima_amc_service_template', {
            'amc_banner_slider_images': amc_banner_slider_images
        })