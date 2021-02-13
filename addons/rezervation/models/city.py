# -*- coding: utf-8 -*-

from odoo import models, fields, api


class City(models.Model):
    _name = 'rezervation.city'
    _description = 'Cities for reservation systems'

    name = fields.Char(size=25, string='Name')
    # country_id = fields.Many2one('rezervation.country', string='Country')

