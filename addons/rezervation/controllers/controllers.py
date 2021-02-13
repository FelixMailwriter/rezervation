# -*- coding: utf-8 -*-
# from odoo import http


# class Rezervation(http.Controller):
#     @http.route('/rezervation/rezervation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rezervation/rezervation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rezervation.listing', {
#             'root': '/rezervation/rezervation',
#             'objects': http.request.env['rezervation.rezervation'].search([]),
#         })

#     @http.route('/rezervation/rezervation/objects/<model("rezervation.rezervation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rezervation.object', {
#             'object': obj
#         })
