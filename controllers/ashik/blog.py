from odoo import http
from odoo.http import request as req


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
