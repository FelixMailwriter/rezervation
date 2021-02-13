# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partners(models.Model):
    _name = 'rezervation.partners'
    _description = 'Partners'
    _rec_name = 'display_name'
    display_name = fields.Char(string='Name', required=True)
    email = fields.Char('Email', required=True)
    mobile = fields.Char('Mobile', required=True)
