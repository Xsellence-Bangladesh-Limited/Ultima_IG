from odoo import http
from odoo.http import request as req


class UltimaWebsite(http.Controller):

    @http.route('/', auth='public')
    def home(self, **kw):
        intro = req.env['ultima.home.introduce'].sudo().search([], limit=1)
        page = req.env['ultima.home'].sudo().search([], limit=1)
        products = req.env['product.template'].sudo().search([
            ('website_publish', '=', True),
            ('detailed_type', '=', 'product'),
        ], limit=3)
        currency_id = req.env.company.currency_id

        testimonials = req.env['ultima.testimonial'].sudo().search([])
        layout = req.env['ultima.layout'].sudo().search([], limit=1)

        print('req.env.user.lang', req.env.user.lang)
        print('req.session.context', req.session.context)

        return req.render('ultima.home', {
            'intro': intro,
            'p': page,
            'products': products,
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

        # lang = req.session
        # req.session.context['age'] = 11

        # print(req.session.context['age'])

        # context = req.session.context
        # context['lang'] = 'bn_IN'

        # session = req.session.context['lang'] = 'bn_IN'
        # http.root.session_store.save(context)

        # print(req.session.context)

        # a = req.session.get('lang')
        # print(a)

        # b = req.env.user.lang = 'bn_IN'
        # print(b)

        # b = req.env.user.lang = 'en_US'
        # print(b)
        #
        # print('req.env.user.lang', req.env.user.lang)
        # lang_code = 'en_US'
        # req.update_context(lang=lang_code)

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
        print('sale_report', sale_report)

        for sr in sale_report:
            print(sr.product_tmpl_id)

        return req.render('ultima.product_details', {
            'product': 'product',
            'testimonials': testimonials,
            'layout': layout,
            'p': page,
        })

    @http.route('/billing', auth='public')
    def billing(self, **kw):
        layout = req.env['ultima.layout'].sudo().search([], limit=1)

        return req.render('ultima.billing', {
            'product': 'product',
            'layout': layout,
        })
