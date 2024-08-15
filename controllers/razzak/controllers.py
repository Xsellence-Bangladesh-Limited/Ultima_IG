from odoo import http
from odoo.http import request as req


class UltimaWebsite(http.Controller):

    @http.route('/', auth='public')
    def home(self, **kw):
        intro = req.env['ultima.home.introduce'].sudo().search([], limit=1)
        page = req.env['ultima.home'].sudo().search([], limit=1)
        products = req.env['product.template'].sudo().search([('detailed_type', '=', 'product')], limit=3)
        currency_id = req.env.company.currency_id

        testimonials = req.env['ultima.testimonial'].sudo().search([])

        return req.render('ultima.home', {
            'intro': intro,
            'p': page,
            'products': products,
            'currency_id': currency_id,
            'testimonials': testimonials,
        })

    @http.route('/products', auth='public')
    def products(self, **kw):
        return req.render('ultima.products', {
            'product': 'product',
        })

    @http.route('/product-details', auth='public')
    def product_details(self, **kw):
        return req.render('ultima.product_details', {
            'product': 'product',
        })

    @http.route('/billing', auth='public')
    def billing(self, **kw):
        return req.render('ultima.billing', {
            'product': 'product',
        })
