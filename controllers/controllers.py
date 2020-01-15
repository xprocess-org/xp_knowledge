# -*- coding: utf-8 -*-
# from odoo import http


# class XpKnowledge(http.Controller):
#     @http.route('/xp_knowledge/xp_knowledge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xp_knowledge/xp_knowledge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xp_knowledge.listing', {
#             'root': '/xp_knowledge/xp_knowledge',
#             'objects': http.request.env['xp_knowledge.xp_knowledge'].search([]),
#         })

#     @http.route('/xp_knowledge/xp_knowledge/objects/<model("xp_knowledge.xp_knowledge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xp_knowledge.object', {
#             'object': obj
#         })
