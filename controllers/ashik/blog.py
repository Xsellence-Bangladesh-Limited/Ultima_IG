from odoo import http
from odoo.http import request as req
from werkzeug.utils import redirect

class Blog(http.Controller):
    @http.route('/blogs', type='http', auth='public')
    def blog(self):

        # Retrieving all the blogs (start)
        all_blogs = req.env['ultima.blog.blog'].sudo().search([], order='id asc')
        # Retrieving all the blogs (end)

        # Retrieving blog slides (start)
        blog_slides = req.env['ultima.blog.slider'].sudo().search([], order='id asc')
        # Retrieving blog slides (end)

        # Retrieving blog categories (start)
        blog_categories = req.env['ultima.blog.category'].sudo().search([], order='id asc')
        # Retrieving blog categories (end)

        blogs_based_on_categories = {category.category_name: [] for category in blog_categories}

        for blog in all_blogs:
            blogs_based_on_categories[blog.category_id.category_name].append(blog)

        print(blogs_based_on_categories)

        return req.render('ultima.ultima_blog_template', {
            'all_blogs': all_blogs,
            'blog_slides': blog_slides,
            'blog_categories': blog_categories,
            'blogs_based_on_categories': blogs_based_on_categories
        })


    @http.route('/blog-details/<int:blog_id>', type='http', auth='public')
    def blog_details(self, blog_id):
        blog = req.env['ultima.blog.blog'].sudo().search([('id', '=', blog_id)])

        suggested_blogs = req.env['ultima.suggested.blog'].sudo().search([('main_blog_id', '=', blog.id)], order='id asc')

        all_suggested_blogs = []

        for s_blog in suggested_blogs:
            for s_s_blog in s_blog.suggested_blog_ids:
                all_suggested_blogs.append(s_s_blog)

        req.session['current_blog'] = blog.id

        query_submission_successful = req.session.get('query_submission_successful')

        req.session['query_submission_successful'] = False

        return req.render('ultima.ultima_blog_details_template', {
            'blog': blog,
            'suggested_blogs': all_suggested_blogs,
            'query_submission_successful': query_submission_successful
        })

    @http.route('/query/user-query', type='http', auth='public', csrf=False)
    def user_query(self, **form_data):
        if req.httprequest.method == 'POST':
            user_name = form_data.get('name_input').strip() if form_data.get('name_input') else ''
            user_email = form_data.get('email_input').strip() if form_data.get('email_input') else ''
            user_mobile = form_data.get('mobile_input').strip() if form_data.get('mobile_input') else ''

            req.env['ultima.blog.query'].sudo().create({
                'user_name': user_name,
                'user_email': user_email,
                'user_mobile': user_mobile
            })

            blog = req.env['ultima.blog.blog'].sudo().search([('id', '=', req.session.get('current_blog'))])

            req.session['query_submission_successful'] = True

            return redirect(f'/blog-details/{blog.id}')

    @http.route('/more-blogs/<string:category_name>', type='http', auth='public')
    def more_blogs(self, category_name):
        category = req.env['ultima.blog.category'].sudo().search([('category_name', '=', category_name)])

        blogs_based_on_category = req.env['ultima.blog.blog'].sudo().search([('category_id', '=', category.id)], order='id asc')
        print(blogs_based_on_category)
        return req.render('ultima.ultima_see_more_blogs_template', {
            'category_name': category_name,
            'blogs_based_on_category': blogs_based_on_category
        })