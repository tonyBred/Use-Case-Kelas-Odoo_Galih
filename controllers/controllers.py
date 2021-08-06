# -*- coding: utf-8 -*-
# from odoo import http


# class LatihanGalih(http.Controller):
#     @http.route('/latihan_galih/latihan_galih/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan_galih/latihan_galih/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan_galih.listing', {
#             'root': '/latihan_galih/latihan_galih',
#             'objects': http.request.env['latihan_galih.latihan_galih'].search([]),
#         })

#     @http.route('/latihan_galih/latihan_galih/objects/<model("latihan_galih.latihan_galih"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan_galih.object', {
#             'object': obj
#         })
