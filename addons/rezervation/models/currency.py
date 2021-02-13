# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Currency(models.Model):
    _name = 'rezervation.currency'
    _description = 'Currency'

    # currency_id = fields.Many2one("rezervation.common_settings", string="Currency_id", on_delete="cascade")
    name = fields.Char(string='Name')
