from odoo import http
from odoo.http import request as req
from werkzeug.utils import redirect
import json

class Blog(http.Controller):
    @http.route('/blogs', type='http', auth='public')
    def blog(self):
        req.session['current_visited_page'] = '/blogs'
        req.session.modified = True

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
        req.session['current_visited_page'] = f'/blog-details/{blog_id}'
        req.session.modified = True

        blog = req.env['ultima.blog.blog'].sudo().search([('id', '=', blog_id)])

        suggested_blogs = req.env['ultima.suggested.blog'].sudo().search([('main_blog_id', '=', blog.id)], order='id asc')

        all_suggested_blogs = []

        for s_blog in suggested_blogs:
            for s_s_blog in s_blog.suggested_blog_ids:
                all_suggested_blogs.append(s_s_blog)

        # req.session['current_blog'] = blog.id

        # query_submission_successful = req.session.get('query_submission_successful')

        # req.session['query_submission_successful'] = False

        ultima_user = req.session.get('ultima_partner_user')

        logged_in_user = req.env['res.partner'].sudo().search([('id', '=', ultima_user), ('website_user', '=', True)])

        if not logged_in_user:
            ultima_user_phone = req.session.get('ultima_user_phone')
            logged_in_user = req.env['res.partner'].sudo().search([('phone', '=', ultima_user_phone), ('website_user', '=', True)])

        all_comments = req.env['ultima.blog.comment'].sudo().search([('blog_id', '=', blog.id)], order='id desc')

        # Retrieving blog page settings (start)
        blog_page_settings = req.env['ultima.blog.settings'].sudo().search([], order='id desc', limit=1)
        # Retrieving blog page settings (end)

        return req.render('ultima.ultima_blog_details_template', {
            'blog': blog,
            'suggested_blogs': all_suggested_blogs,
            # 'query_submission_successful': query_submission_successful,
            'logged_in_user': logged_in_user,
            'all_comments': all_comments,
            'logged_in_user_id': logged_in_user.id,
            'blog_page_settings': blog_page_settings
        })

    @http.route('/query/user-query', type='http', auth='public', csrf=False)
    def user_query(self, **form_data):
        if req.httprequest.method == 'POST':
            user_name = form_data.get('nameInput').strip() if form_data.get('nameInput') else ''
            user_email = form_data.get('emailInput').strip() if form_data.get('emailInput') else ''
            user_mobile = form_data.get('mobileInput').strip() if form_data.get('mobileInput') else ''
            blog_id = int(form_data.get('blogID')) if form_data.get('blogID') else None

            req.env['ultima.blog.query'].sudo().create({
                'user_name': user_name,
                'user_email': user_email,
                'user_mobile': user_mobile,
                'blog_id': blog_id
            })

            # blog = req.env['ultima.blog.blog'].sudo().search([('id', '=', req.session.get('current_blog'))])

            # req.session['query_submission_successful'] = True

            # return redirect(f'/blog-details/{blog_id}')

            return json.dumps({'code': 200})

    @http.route('/comments/user-comment', type='http', auth='user', csrf=False)
    def user_comment(self, **form_data):
        comment = form_data.get('comment').strip() if form_data.get('comment') else ''
        blog_id = int(form_data.get('blogId')) if form_data.get('blogId') else None

        ultima_user = req.session.get('ultima_partner_user')

        logged_in_user = req.env['res.partner'].sudo().search([('id', '=', ultima_user)])

        if not logged_in_user:
            ultima_user_phone = req.session.get('ultima_user_phone')
            logged_in_user = req.env['res.partner'].sudo().search([('phone', '=', ultima_user_phone)])

        # Creating a new comment (start)

        new_comment = req.env['ultima.blog.comment'].sudo().create({
            'comment': comment,
            'user_id': logged_in_user.id,
            'blog_id': blog_id
        })

        # Creating a new comment (end)

        # Retrieving all comments (start)

        all_comments_l_5 = req.env['ultima.blog.comment'].sudo().search([('blog_id', '=', blog_id)], order='id desc', limit=5)
        total_number_of_comments = req.env['ultima.blog.comment'].sudo().search_count([])

        comment_dict_list = []

        for s_comment in all_comments_l_5:
            comment_dict_list.append({
                'user_id': s_comment.user_id.id,
                'user_name': s_comment.user_id.name,
                'comment': s_comment.comment,
                'image_available': True if s_comment.user_id.image_1920 else False
            })

        # Retrieving all comments (end)

        if new_comment:
            return json.dumps({'code': 200, 'all_comments_l_5': comment_dict_list, 'total_number_of_comments': total_number_of_comments})

    @http.route('/more-blogs/<string:category_name>', type='http', auth='public')
    def more_blogs(self, category_name):
        category = req.env['ultima.blog.category'].sudo().search([('category_name', '=', category_name)])

        blogs_based_on_category = req.env['ultima.blog.blog'].sudo().search([('category_id', '=', category.id)], order='id asc')
        print(blogs_based_on_category)
        return req.render('ultima.ultima_see_more_blogs_template', {
            'category_name': category_name,
            'blogs_based_on_category': blogs_based_on_category
        })