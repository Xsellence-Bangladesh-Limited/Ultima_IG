from odoo import http
from odoo.http import request as req
from werkzeug.utils import redirect


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

    @http.route('/billing', auth='public', csrf=False)
    def billing(self, **kw):
        if req.httprequest.method == 'POST':
            form_product_id = int(kw.get('product_id')) if kw.get('product_id') else None
            full_name = kw.get('full_name').strip() if kw.get('full_name') else ''
            phone_number = kw.get('phone_number').strip() if kw.get('phone_number') else ''
            email_address = kw.get('email_address').strip() if kw.get('email_address') else ''
            address = kw.get('address').strip() if kw.get('address') else ''
            order_note = kw.get('order_note').strip() if kw.get('order_note') else ''
            shipping_location = kw.get('shipping_location').strip() if kw.get('shipping_location') else ''
            shipping_type = kw.get('shipping_type').strip() if kw.get('shipping_type') else ''
            otp = kw.get('otp').strip() if kw.get('otp') else ''

            product_obj = req.env['product.product'].sudo().search([('product_tmpl_id', '=', form_product_id)])

            # [(4, other_guiding_area_id) for other_guiding_area_id in other_guiding_area_ids]

            # Creating a new order (start)

            new_order = req.env['ultima.product.order'].sudo().create({
                'full_name': full_name,
                'phone_number': phone_number,
                'email_address': email_address,
                'address': address,
                'user_id': req.env.user.id,
                'order_note': order_note,
                'shipping_location': shipping_location,
                'shipping_type': shipping_type,
                'otp': otp,
                'product_ids': [(4, product_obj.id)]
            })

            if new_order:
                logged_in_user = req.env['res.users'].sudo().search([('id', '=', req.env.user.id)])

                new_sale_order = req.env['sale.order'].sudo().create({
                    'partner_id': logged_in_user.partner_id.id,
                    'order_line': [
                        (0, 0, {
                            'product_id': product.id,
                            'product_uom_qty': 1,
                            'price_unit': product.list_price
                        }) for product in new_order.product_ids
                    ]
                })

                if new_sale_order:
                    return redirect('/order-completed')

            # Creating a new order (end)


        layout = req.env['ultima.layout'].sudo().search([], limit=1)

        product_id = int(kw.get('product_id')) if kw.get('product_id') else None

        logged_in_user = req.env['res.users'].sudo().search([('id', '=', req.env.user.id)])

        return req.render('ultima.billing', {
            'product': 'product',
            'product_id': product_id,
            'layout': layout,
            'logged_in_user': logged_in_user
        })

    @http.route('/order-completed', auth='public')
    def complete_order(self):
        return req.render('ultima.ultima_order_completion_template', {})
