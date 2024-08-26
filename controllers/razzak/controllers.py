from odoo import http
from odoo.http import request as req


class UltimaWebsite(http.Controller):

    @http.route('/', auth='public')
    def home(self, **kw):
        intro = req.env['ultima.home.introduce'].sudo().search([], limit=1)
        page = req.env['ultima.home'].sudo().search([], limit=1)

        # Best Selling Products
        # products = req.env['product.template'].sudo().search([
        #     ('website_publish', '=', True),
        #     ('detailed_type', '=', 'product'),
        # ], limit=3)

        currency_id = req.env.company.currency_id

        testimonials = req.env['ultima.testimonial'].sudo().search([])
        layout = req.env['ultima.layout'].sudo().search([], limit=1)

        return req.render('ultima.home', {
            'intro': intro,
            'p': page,
            # 'products': products,
            'currency_id': currency_id,
            'testimonials': testimonials,
            'layout': layout,
        })

    @http.route('/products', auth='public')
    def products(self, **kw):
        layout = req.env['ultima.layout'].sudo().search([], limit=1)
        page = req.env['ultima.products'].sudo().search([], limit=1)
        currency_id = req.env.company.currency_id
        testimonials = req.env['ultima.testimonial'].sudo().search([])
        products = req.env['product.template'].sudo().search([
            ('website_publish', '=', True),
            ('detailed_type', '=', 'product'),
        ])

        return req.render('ultima.products', {
            'p': page,
            'currency_id': currency_id,
            'products': products,
            'testimonials': testimonials,
            'layout': layout,
        })

    @http.route('/product-details', auth='public')
    def product_details(self, **kw):

        layout = req.env['ultima.layout'].sudo().search([], limit=1)
        testimonials = req.env['ultima.testimonial'].sudo().search([])
        page = req.env['ultima.pd_detail'].sudo().search([], limit=1)

        sale_report = req.env['sale.report'].sudo().search([])

        # Product
        product_id = kw.get('id')
        if not product_id:
            return 'Product id not passed'
        
        product = req.env['product.template'].sudo().search([('id', '=', int(product_id))])
        if not product:
            return 'Product object not found'

        currency_id = req.env.company.currency_id

        return req.render('ultima.product_details', {
            'product': product,
            'pd': product,
            'testimonials': testimonials,
            'layout': layout,
            'p': page,
            'currency_id': currency_id,
        })

    @http.route('/billing', auth='public')
    def billing(self, **kw):
        layout = req.env['ultima.layout'].sudo().search([], limit=1)

        return req.render('ultima.billing', {
            'product': 'product',
            'layout': layout,
        })
