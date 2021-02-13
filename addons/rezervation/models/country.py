# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Country(models.Model):
    _name = 'rezervation.country'
    _description = 'Country for reservation systems'

    country_id = fields.Many2one("rezervation.user", string="country_id", ondelete='cascade')
    name = fields.Char(size=25, string='Name')