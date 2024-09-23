from odoo import http
from odoo.http import request as req

import json


class UserPanel(http.Controller):
    @http.route('/user-panel', type='http', auth='public')
    def user_panel(self):
        ultima_user = req.session.get('ultima_partner_user')

        logged_in_user = req.env['res.partner'].sudo().search([('id', '=', ultima_user), ('website_user', '=', True)])

        if not logged_in_user:
            ultima_user_phone = req.session.get('ultima_user_phone')
            logged_in_user = req.env['res.partner'].sudo().search([('phone', '=', ultima_user_phone), ('website_user', '=', True)])

        # Retrieving orders (start)
        all_orders = req.env['ultima.product.order'].sudo().search([('user_id', '=', logged_in_user.id)], order='id desc')
        # Retrieving orders (end)

        return req.render('ultima.user_panel_template', {
            'logged_in_user': logged_in_user,
            'all_orders': all_orders,
            'currency': req.env.company.currency_id.symbol,
        })

    @http.route('/product-details-ajax', type='http', auth='public', csrf=False)
    def product_details(self, **kw):
        product_id = int(kw.get('productID')) if kw.get('productID') else None
        order_id = int(kw.get('orderID')) if kw.get('orderID') else None

        order = req.env['ultima.product.order'].sudo().search([('id', '=', order_id)])

        product = req.env['product.product'].sudo().search([('id', '=', product_id)])
        product_tmpl = req.env['product.template'].sudo().search([('id', '=', product.product_tmpl_id.id)])
        currency_id = req.env.company.currency_id

        data = {
            'product_id': product_tmpl.id,
            'product_name': product_tmpl.name,
            'total_price': f'{currency_id.symbol}{order.total_price}',
            'order_name': order.name,
            'order_date': order.format_order_date()
        }

        return json.dumps({'code': 200, 'data': data})
