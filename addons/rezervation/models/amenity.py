# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Amenity(models.Model):
    _name = 'rezervation.amenity'
    _description = 'Amenity for the accomodation object'

    # amenity_id = fields.Many2one("rezervation.flat", string="Amenity_id", ondelete='cascade')
    amenity_name = fields.Char(size=50, string="Amenity's name", required=True)
    type = fields.Char(string="Type")
    icon = fields.Binary(string='Icon')

