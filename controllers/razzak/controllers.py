import json

from odoo import http
from odoo.http import request as req
from werkzeug.utils import redirect

from sslcommerz_lib import SSLCOMMERZ

class UltimaWebsite(http.Controller):

    @http.route('/', auth='public')
    def home(self, **kw):

        # Toggling language in session (start)
        session = req.session.context
        cur_lang = session.get('lang')
        if cur_lang == 'bn_IN':
            session['lang'] = 'en_US'

        elif cur_lang == 'en_US':
            session['lang'] = 'bn_IN'

        print(session.get('lang'))
        # Toggling language in session (end)

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

        if intro.section_bg_color:
            hex_color = intro.section_bg_color.lstrip('#')
            intro_section_bg_color_rgb = list(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

            if intro.section_bg_opacity:
                intro_section_bg_color_rgb.append(intro.section_bg_opacity)
                intro_section_bg_color = tuple(intro_section_bg_color_rgb)

            else:
                intro_section_bg_color = intro.section_bg_color

        else:
            intro_section_bg_color = 'transparent'

        return req.render('ultima.home', {
            'intro': intro,
            'intro_section_bg_color': intro_section_bg_color,
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
            'product_extra_images': list(product.product_template_image_ids) + [product]
        })

    @http.route('/billing', auth='public', csrf=False)
    def billing(self, **kw):
        base_url = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        form_product_id = int(kw.get('product_id')) if kw.get('product_id') else None
        product_obj = req.env['product.product'].sudo().search([('product_tmpl_id', '=', form_product_id)])

        if req.httprequest.method == 'POST':
            product_total_price = float(kw.get('product_total_price')) if kw.get('product_total_price') else 0
            cart_total_price = float(kw.get('product_total_price')) if kw.get('product_total_price') else 0
            number_of_product = int(kw.get('number_of_product')) if kw.get('number_of_product') else 1

            full_name = kw.get('full_name').strip() if kw.get('full_name') else ''
            phone_number = kw.get('phone_number').strip() if kw.get('phone_number') else ''
            email_address = kw.get('email_address').strip() if kw.get('email_address') else ''
            address = kw.get('address').strip() if kw.get('address') else ''
            order_note = kw.get('order_note').strip() if kw.get('order_note') else ''
            shipping_location = kw.get('shipping_location').strip() if kw.get('shipping_location') else ''
            shipping_type = kw.get('shipping_type').strip() if kw.get('shipping_type') else ''
            otp = kw.get('otp').strip() if kw.get('otp') else ''

            # [(4, other_guiding_area_id) for other_guiding_area_id in other_guiding_area_ids]

            # Making payment (start)
            settings = {'store_id': 'ultim66e5881171fa2', 'store_pass': 'ultim66e5881171fa2@ssl', 'issandbox': True}
            sslcz = SSLCOMMERZ(settings)
            post_body = {}
            post_body['total_amount'] = cart_total_price
            post_body['currency'] = "BDT"
            post_body['tran_id'] = "12345"
            post_body['success_url'] = f"{base_url}/order-completed"
            post_body['fail_url'] = f"{base_url}/payment-failed"
            post_body['cancel_url'] = f"{base_url}/payment-failed"
            post_body['emi_option'] = 0
            post_body['cus_name'] = req.env.user.partner_id.name
            post_body['cus_email'] = req.env.user.partner_id.email
            post_body['cus_phone'] = req.env.user.partner_id.phone
            post_body['cus_add1'] = req.env.user.partner_id.country_id.name
            post_body['cus_city'] = req.env.user.partner_id.country_id.name
            post_body['cus_country'] = req.env.user.partner_id.country_id.name
            post_body['shipping_method'] = "NO"
            post_body['multi_card_name'] = ""
            post_body['num_of_item'] = number_of_product
            post_body['product_name'] = product_obj.name
            post_body['product_category'] = "Test Category"
            post_body['product_profile'] = "general"

            response = sslcz.createSession(post_body)
            # Making payment (end)

            # Creating a new order (start)

            if response.get('status') == 'SUCCESS':
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
                    'product_ids': [(4, product_obj.id)],
                    'total_price': cart_total_price,
                    'product_qty': number_of_product
                })

                if new_order:
                    logged_in_user = req.env['res.users'].sudo().search([('id', '=', req.env.user.id)])

                    new_sale_order = req.env['sale.order'].sudo().create({
                        'partner_id': logged_in_user.partner_id.id,
                        'order_line': [
                            (0, 0, {
                                'product_id': product.id,
                                'product_uom_qty': number_of_product,
                                'price_unit': product.list_price
                            }) for product in new_order.product_ids
                        ]
                    })

                    if new_sale_order:
                        return redirect(response.get('GatewayPageURL'))

            # Creating a new order (end)


        layout = req.env['ultima.layout'].sudo().search([], limit=1)

        product_id = int(kw.get('product_id')) if kw.get('product_id') else None

        logged_in_user = req.env['res.users'].sudo().search([('id', '=', req.env.user.id)])

        currency_id = req.env.company.currency_id

        return req.render('ultima.billing', {
            'product': product_obj,
            'product_id': product_id,
            'layout': layout,
            'logged_in_user': logged_in_user,
            'currency_id': currency_id
        })

    @http.route('/order-completed', type='http', auth='public', method=['GET', 'POST'], csrf=False)
    def complete_order(self, **kw):
        paid_amount = kw.get('amount')
        card_type = kw.get('card_type')
        bank_tran_id = kw.get('bank_tran_id')
        transaction_date = kw.get('tran_date')
        currency = kw.get('currency')
        card_issuer = kw.get('card_issuer')
        card_no = kw.get('card_no')
        card_brand = kw.get('card_brand')
        card_issuer_country = kw.get('card_issuer_country')
        store_id = kw.get('store_id')
        existing_payment = req.env['ultima.payment'].sudo().search_count([('bank_tran_id', '=', bank_tran_id)])
        if bank_tran_id and not existing_payment:
            new_payment = req.env['ultima.payment'].sudo().create({
                # 'user': req.env.user.id,
                'paid_amount': paid_amount,
                'card_type': card_type,
                'bank_tran_id': bank_tran_id,
                'transaction_date': transaction_date,
                'currency': currency,
                'card_issuer': card_issuer,
                'card_no': card_no,
                'card_brand': card_brand,
                'card_issuer_country': card_issuer_country,
                'store_id': store_id
            })

            if new_payment:
                return req.render('ultima.ultima_order_completion_template', {})
        else:
            return 'Something went wrong. Are you trying to repay?'

    @http.route('/payment-failed', type='http', auth='public', method=['GET', 'POST'], csrf=False)
    def payment_failed(self, **kw):
        return 'Payment failed.'

    @http.route('/send-expert-message', type='http', auth='public', csrf=False)
    def send_expert_message(self, **form_data):
        user_name = form_data.get('userName').strip() if form_data.get('userName') else None
        phone_number = form_data.get('phoneNumber').strip() if form_data.get('phoneNumber') else None

        # Creating a new expert message (start)

        req.env['ultima.expert.message'].sudo().create({
            'user_name': user_name,
            'user_phone_number': phone_number
        })

        # Creating a new expert message (end)

        return json.dumps({'code': 200})


