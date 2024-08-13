from odoo import http
from odoo.http import request as req


class Controllers(http.Controller):
    @http.route('/aaa', type='http', auth='public')
    def aaa(self):
        return 'aaa'
