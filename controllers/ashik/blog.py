from odoo import http
from odoo.http import request as req


class Blog(http.Controller):
    @http.route('/blogs', type='http', auth='public')
    def blog(self):
        return req.render('ultima.ultima_blog_template', {})