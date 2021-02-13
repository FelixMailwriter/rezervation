# -*- coding: utf-8 -*-

from odoo import models, fields


class Flat(models.Model):
    _name = 'rezervation.flat'
    _description = 'Flats for reservation systems'

    inner_id = fields.Char(size=15, string='Inner id')
    flat_type = fields.Char(size=15, string="Flat's type", required=True)
    rooms_qty = fields.Integer(string='Rooms', required=True)
    beds_qty = fields.Integer(string='Beds', required=True)
    area = fields.Float(string='Area', digits=(6, 2))
    city = fields.Char(size=15, string='City', required=True)
    district = fields.Char(siae=15, string='District', required=True)
    address = fields.Text(string='Address', required=True)
    site = fields.Char(size=255, string='www')
    floor = fields.Integer(string='Floor', required=True)
    manager = fields.Char(siae=15, string='Manager', required=True)
    manager_phone = fields.Char(siae=15, string="Manager's phone", required=True)
    description = fields.Text(string='Description')
    lon = fields.Char(siae=15, string='Lon', required=True)
    lat = fields.Char(siae=15, string='Lat', required=True)
    how_to_get = fields.Text(string='How to get')
    min_staying = fields.Integer(string='Minimal staying')
    standard_price = fields.Float(string='Price per day', digits = (6,2), required = True)
    extra_pay_guest_qty = fields.Integer(string='Number of guests for extra pay')
    extra_pay = fields.Integer(string='Extra pay')
    extra_pay_dimension = fields.Selection([('persent', '%'), ('euro', 'Euro')], string='Dimension')
    breakfast_included = fields.Boolean(string='Breakfast')
    deleted = fields.Boolean(string='Deleted')
    # amenities = fields.One2many("rezervation.amenity", "amenity_id", string="Amenities")
