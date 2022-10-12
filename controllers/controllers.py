# -*- coding: utf-8 -*-
from odoo import http

# class MethodPaymentTermPurchase(http.Controller):
#     @http.route('/method_payment_term_purchase/method_payment_term_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_payment_term_purchase/method_payment_term_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_payment_term_purchase.listing', {
#             'root': '/method_payment_term_purchase/method_payment_term_purchase',
#             'objects': http.request.env['method_payment_term_purchase.method_payment_term_purchase'].search([]),
#         })

#     @http.route('/method_payment_term_purchase/method_payment_term_purchase/objects/<model("method_payment_term_purchase.method_payment_term_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_payment_term_purchase.object', {
#             'object': obj
#         })