# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrdenCompra(models.Model):
    _inherit = 'purchase.order'
    _description = 'Agregar plazo de pago a OC'
    
    plazo_pago_id = fields.Many2one('account.payment.term', string='Plazo de Pago')

    @api.onchange('partner_id')
    def _onchange_(self):
        self.plazo_pago_id=self.partner_id.property_supplier_payment_term_id.id