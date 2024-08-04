from odoo import http
from odoo.http import request as req

class AboutUs(http.Controller):
    @http.route('/about-us', type='http', auth='public')
    def about_us(self):

        # Retrieving the clients (start)
        about_us_clients = req.env['ultima.about.us.client'].sudo().search([], order='id asc')
        # Retrieving the clients (end)

        # Retrieving the features (start)
        about_us_features = req.env['ultima.about.us.feature'].sudo().search([], order='id asc')
        # Retrieving the features (end)

        # Retrieving the offers (start)
        about_us_offers = req.env['ultima.about.us.offer'].sudo().search([], order='id asc')
        # Retrieving the offers (end)

        return req.render('ultima.ultima_about_us_template', {
            'about_us_clients': about_us_clients,
            'about_us_features': about_us_features,
            'about_us_offers': about_us_offers
        })
