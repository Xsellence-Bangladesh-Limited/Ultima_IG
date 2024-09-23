import json, random, time, requests

from odoo import http
from odoo.http import request as req
from werkzeug.utils import redirect

from sslcommerz_lib import SSLCOMMERZ

class UltimaWebsite(http.Controller):

    @http.route('/create-otp', type='http', auth='public', csrf=False)
    def create_otp(self, **kw):
        # session = req.session.context

        phone_number = kw.get('phoneNumber').strip() if kw.get('phoneNumber') else ''

        random_generated_otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])

        req.session['ultima_otp'] = random_generated_otp
        req.session.modified = True

        print('hmm', req.session.get('ultima_otp'))

        sms_settings = req.env['ultima.sms.settings'].sudo().search([], order='id desc', limit=1)

        if phone_number:
            data = {
                'api_key': sms_settings.api_key if sms_settings.api_key else 'C200918366ebcc11bc0e03.88783932',
                'type': 'unicode',
                'contacts': f"880{phone_number[-10:]}",
                'senderid': '8809601011978',
                'msg': sms_settings.message.format(random_generated_otp) if sms_settings.message else f"Hello Dear Customer, Your Ultima Bangladesh One Time PIN is {random_generated_otp}."
            }

            r = requests.post(
                f"https://msg.elitbuzz-bd.com/smsapi", json=data)

            if r.status_code == 200:
                return json.dumps({'code': 200})

    @http.route('/register-user', type='http', auth='public', csrf=False)
    def register_user(self, **kw):
        first_name = kw.get('firstName').strip() if kw.get('firstName') else ''
        # last_name = kw.get('lastName').strip() if kw.get('lastName') else ''
        email_address = kw.get('emailAddress').strip() if kw.get('emailAddress') else ''

        email_exists = req.env['res.partner'].sudo().search([('email', '=', email_address), ('website_user', '=', True)])

        if email_exists:
            return json.dumps({'code': 400})

        phone_number = kw.get('phoneNumber').strip() if kw.get('phoneNumber') else ''

        # Creating a new partner (start)
        new_partner = req.env['res.partner'].sudo().create({
            'name': first_name,
            'phone': phone_number,
            'mobile': phone_number,
            'email': email_address,
            'website_user': True
        })

        req.session['ultima_partner_user'] = new_partner.id
        req.session['ultima_user_phone'] = phone_number

        req.session.modified = True

        if new_partner:
            req.session['ultima_otp'] = None
            req.session.modified = True
            current_page = req.session.get('current_visited_page')
            return json.dumps({'code': 200, 'current_page': current_page})

        # Creating a new partner (start)

    @http.route('/check-otp', type='http', auth='public', csrf=False)
    def check_otp(self, **kw):
        otp = kw.get('otp').strip() if kw.get('otp') else None
        phone_number = kw.get('phoneNumber').strip() if kw.get('phoneNumber') else ''

        req.session['ultima_user_phone'] = phone_number

        existing_user = req.env['res.partner'].sudo().search([('phone', '=', phone_number), ('website_user', '=', True)])

        session_otp = req.session.get('ultima_otp')

        if session_otp == otp and not existing_user:
            return json.dumps({'code': 200})

        elif session_otp == otp and existing_user:
            current_page = req.session.get('current_visited_page')
            print(current_page)
            return json.dumps({'code': 201, 'current_page': current_page})
        else:
            return json.dumps({'code': 400})

    @http.route('/log-out-user', type='http', auth='public', csrf=False)
    def log_out_user(self):
        req.session['ultima_partner_user'] = None
        req.session['ultima_user_phone'] = None
        req.session['current_visited_page'] = '/'
        req.session.modified = True

        return redirect('/')

    @http.route('/', auth='public')
    def home(self, **kw):

        # req.session['current_visited_page'] = '/'
        # req.session.modified = True

        # print('hmm-home', req.session.get('ultima_otp'))

        # Toggling language in session (start)
        # session = req.session.context
        # cur_lang = session.get('lang')
        # if cur_lang == 'bn_IN':
        #     session['lang'] = 'en_US'
        #
        # elif cur_lang == 'en_US':
        #     session['lang'] = 'bn_IN'
        #
        # print(session.get('lang'))
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
        # req.session['current_visited_page'] = '/products'
        # req.session.modified = True

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
        product_id = kw.get('id')

        req.session['current_visited_page'] = f'/product-details?id={product_id}'
        req.session.modified = True

        layout = req.env['ultima.layout'].sudo().search([], limit=1)
        testimonials = req.env['ultima.testimonial'].sudo().search([])
        page = req.env['ultima.pd_detail'].sudo().search([], limit=1)
        page_products = req.env['ultima.products'].sudo().search([], limit=1)

        sale_report = req.env['sale.report'].sudo().search([])

        # Product
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
            'pp': page_products,
            'currency_id': currency_id,
            'product_extra_images': list(product.product_template_image_ids) + [product],
            'product_videos': product.video_ids
        })

    @http.route('/billing', auth='public', csrf=False)
    def billing(self, **kw):
        ultima_user = req.session.get('ultima_partner_user')
        logged_in_user = req.env['res.partner'].sudo().search([('id', '=', ultima_user), ('website_user', '=', True)])

        if not logged_in_user:
            ultima_user_phone = req.session.get('ultima_user_phone')
            logged_in_user = req.env['res.partner'].sudo().search([('phone', '=', ultima_user_phone), ('website_user', '=', True)])

        base_url = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        form_product_id = int(kw.get('product_id')) if kw.get('product_id') else None
        product_obj = req.env['product.product'].sudo().search([('product_tmpl_id', '=', form_product_id)])
        shipping_types = req.env['ultima.payment.shipping.type'].sudo().search([], order='id asc')

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
            shipping_cost = float(kw.get('shipping_cost')) if kw.get('shipping_cost') else 0
            payment_method = kw.get('payment_method').strip() if kw.get('payment_method') else ''
            otp = kw.get('otp').strip() if kw.get('otp') else ''

            # [(4, other_guiding_area_id) for other_guiding_area_id in other_guiding_area_ids]

            if payment_method == 'cash_on_delivery':
                new_order = req.env['ultima.product.order'].sudo().create({
                    'full_name': full_name,
                    'phone_number': phone_number,
                    'email_address': email_address,
                    'address': address,
                    'user_id': logged_in_user.id,
                    'order_note': order_note,
                    'shipping_location': shipping_location,
                    'shipping_type': shipping_type,
                    'payment_method': 'cash_on_delivery',
                    'otp': otp,
                    'product_ids': [(4, product_obj.id)],
                    'total_price': cart_total_price,
                    'product_qty': number_of_product
                })

                if new_order:
                    shipping_service_product = req.env['product.product'].sudo().search([('default_code', '=', 'ULTIMA_WEB_PROD_SHIPPING_COST')])

                    if not shipping_service_product:
                        shipping_service_product = req.env['product.product'].sudo().create({
                            'name': 'Ultima web product shipping cost',
                            'detailed_type': 'service',
                            'list_price': 0,
                            'default_code': 'ULTIMA_WEB_PROD_SHIPPING_COST'
                        })

                    new_sale_order = req.env['sale.order'].sudo().create({
                        'partner_id': logged_in_user.id,
                        'order_line': [
                            (0, 0, {
                                'product_id': product.id,
                                'product_uom_qty': number_of_product,
                                'price_unit': product.list_price
                            }) for product in new_order.product_ids
                        ]
                    })

                    shipping_service_product.sudo().write({
                        'list_price': shipping_cost
                    })

                    new_sale_order.sudo().write({
                        'order_line': [(0, 0, {
                                'product_id': shipping_service_product.id,
                                'product_uom_qty': 1,
                                'price_unit': shipping_service_product.list_price
                            })]
                    })

                    req.env.cr.commit()

                    if new_sale_order:
                        return redirect('/order-completed?pay=cash')

            else:
                # Making payment (start)
                ultima_sslcommerz_tokens = req.env['ultima.sslcommerz.token'].sudo().search([], order='id desc', limit=1)

                store_id = ultima_sslcommerz_tokens.store_id if ultima_sslcommerz_tokens and ultima_sslcommerz_tokens.store_id else 'ultim66e5881171fa2'
                store_pass = ultima_sslcommerz_tokens.store_pass if ultima_sslcommerz_tokens and ultima_sslcommerz_tokens.store_pass else 'ultim66e5881171fa2@ssl'

                settings = {'store_id': store_id, 'store_pass': store_pass, 'issandbox': True}
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
                post_body['csrf_token'] = req.csrf_token()

                response = sslcz.createSession(post_body)
                # Making payment (end)

                # Creating a new order (start)

                if response.get('status') == 'SUCCESS':
                    new_order = req.env['ultima.product.order'].sudo().create({
                        'full_name': full_name,
                        'phone_number': phone_number,
                        'email_address': email_address,
                        'address': address,
                        'user_id': logged_in_user.id,
                        'order_note': order_note,
                        'shipping_location': shipping_location,
                        'shipping_type': shipping_type,
                        'payment_method': 'sslcommerz',
                        'otp': otp,
                        'product_ids': [(4, product_obj.id)],
                        'total_price': cart_total_price,
                        'product_qty': number_of_product
                    })

                    if new_order:
                        shipping_service_product = req.env['product.product'].sudo().search(
                            [('default_code', '=', 'ULTIMA_WEB_PROD_SHIPPING_COST')])

                        if not shipping_service_product:
                            shipping_service_product = req.env['product.product'].sudo().create({
                                'name': 'Ultima web product shipping cost',
                                'detailed_type': 'service',
                                'list_price': 0,
                                'default_code': 'ULTIMA_WEB_PROD_SHIPPING_COST'
                            })

                        new_sale_order = req.env['sale.order'].sudo().create({
                            'partner_id': logged_in_user.id,
                            'order_line': [
                                (0, 0, {
                                    'product_id': product.id,
                                    'product_uom_qty': number_of_product,
                                    'price_unit': product.list_price
                                }) for product in new_order.product_ids
                            ]
                        })

                        shipping_service_product.sudo().write({
                            'list_price': shipping_cost
                        })

                        new_sale_order.sudo().write({
                            'order_line': [(0, 0, {
                                'product_id': shipping_service_product.id,
                                'product_uom_qty': 1,
                                'price_unit': shipping_service_product.list_price
                            })]
                        })

                        req.env.cr.commit()

                        if new_sale_order:
                            return redirect(response.get('GatewayPageURL'))

            # Creating a new order (end)

        layout = req.env['ultima.layout'].sudo().search([], limit=1)

        product_id = int(kw.get('product_id')) if kw.get('product_id') else None

        currency_id = req.env.company.currency_id

        return req.render('ultima.billing', {
            'product': product_obj,
            'product_id': product_id,
            'layout': layout,
            'logged_in_user': logged_in_user,
            'currency_id': currency_id,
            'shipping_types': shipping_types
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
            if kw.get('pay') == 'cash':
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

    @http.route('/update-current-page-for-buy-now', type='http', auth='public', csrf=False)
    def update_current_path_for_buy_now(self, **kw):
        print('buy now called')
        product_id = kw.get('productId')
        req.session['current_visited_page'] = f'/billing?product_id={product_id}'
        req.session.modified = True

        return json.dumps({'code': 200})
