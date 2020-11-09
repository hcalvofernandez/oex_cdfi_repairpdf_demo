# -*- coding: utf-8 -*-

from odoo import models, fields, api,tools

class Facturacion(models.Model):
    _name = "account.invoice"
    _inherit = "account.invoice"

    discount_rate = fields.Float("Tasa de descuento",default=0)#Tasa de descuento


