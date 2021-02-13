# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Currency(models.Model):
    _name = 'rezervation.user_types'
    _description = "User's types"

    # user_type_id = fields.Many2many("rezervation.common_settings", )
    name = fields.Char(string='Name of type')
