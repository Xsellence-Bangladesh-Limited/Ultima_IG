from odoo import http
from odoo.http import request as req

# OTP practice (start)

# import pyotp
import time

import json


# totp = pyotp.TOTP('base32secret3232')
# a = totp.now()
#
# print(totp.verify(a))
# time.sleep(30)
# print(totp.verify(a))

# OTP practice (end)


class TestSession(http.Controller):
    @http.route('/test-session', type='http', auth='public')
    def test_session(self):
        # # Selected language
        # selected_language = req.env['res.lang'].sudo().search([('code', '=', 'bn_IN')])
        # selected_language = req.env['res.lang'].sudo().search([('code', '=', 'en_US')])
        #
        # # Selected user
        # selected_user = req.env['res.users'].sudo().search([('login', '=', 'admin')])
        #
        # print(selected_user._fields)
        #
        # selected_user.sudo().write({
        #     'lang': selected_language.code
        # })
        #
        # req.env.cr.commit()
        #
        session = req.session.context
        #
        # print(req.default_lang())
        #
        # session['lang'] = 'bn_IN'
        #
        # print(req.default_lang())

        # session['ultima_user'] = 2

        return req.render('ultima.test_session_template', {
            'session': session
        })

# class TestAttendance(http.Controller):
#     @http.route(['/test-attendance'], type='json', auth='none')
#     def test_attendance(self, **kw):
#         print('called')
#         return json.dumps({'Success': 200, 'Hmm': 201})