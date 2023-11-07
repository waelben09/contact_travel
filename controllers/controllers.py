# -*- coding: utf-8 -*-
# from odoo import http


# class ContactTravel(http.Controller):
#     @http.route('/contact_travel/contact_travel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_travel/contact_travel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_travel.listing', {
#             'root': '/contact_travel/contact_travel',
#             'objects': http.request.env['contact_travel.contact_travel'].search([]),
#         })

#     @http.route('/contact_travel/contact_travel/objects/<model("contact_travel.contact_travel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_travel.object', {
#             'object': obj
#         })
