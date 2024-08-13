from odoo import http
from odoo.http import request as req


class UltimaWebsite(http.Controller):

    @http.route('/', auth='public')
    def home(self, **kw):
        return req.render('ultima.home', {
            'product': 'product',
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
