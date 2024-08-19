from odoo import http
from odoo.http import request as req

class TestSession(http.Controller):
    @http.route('/test-session', type='http', auth='public')
    def test_session(self):
        # Selected language
        selected_language = req.env['res.lang'].sudo().search([('code', '=', 'bn_IN')])
        # selected_language = req.env['res.lang'].sudo().search([('code', '=', 'en_US')])

        # Selected user
        selected_user = req.env['res.users'].sudo().search([('login', '=', 'admin')])

        # print(selected_user._fields)

        # selected_user.sudo().write({
        #     'lang': selected_language.code
        # })

        # req.env.cr.commit()

        session = req.session.context

        print(req.default_lang())

        # session['lang'] = 'bn_IN'

        print(req.default_lang())

        return req.render('ultima.test_session_template', {
            'session': session
        })

