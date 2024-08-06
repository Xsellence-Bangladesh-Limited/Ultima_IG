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

        # Retrieving the growth data (start)
        about_us_growth_data = req.env['ultima.about.us.growth.data'].sudo().search([], order='id asc')
        # Retrieving the growth data (end)

        # Retrieving the offers (start)
        about_us_offers = req.env['ultima.about.us.offer'].sudo().search([], order='id asc')
        # Retrieving the offers (end)

        # Retrieving the page settings (start)
        about_us_settings = req.env['ultima.about.us.settings'].sudo([], order='id desc', limit=1)
        # Retrieving the page settings (end)

        return req.render('ultima.ultima_about_us_template', {
            'about_us_clients': about_us_clients,
            'about_us_features': about_us_features,
            'about_us_growth_data': about_us_growth_data,
            'about_us_offers': about_us_offers,
            'about_us_settings': about_us_settings
        })
