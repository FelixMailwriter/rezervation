# -*- coding: utf-8 -*-

from odoo import models, fields, api


class User(models.Model):
    _name = 'rezervation.user'
    _description = 'User'


    first_name = fields.Char(size=25, string='First name')
    last_name = fields.Char(size=15, string="Last name", required=True)
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], string='Sex')
    registration_date = fields.Date(string="Registration date")
    birthday = fields.Date(string = "Birthday")
    phone = fields.Char(size=15, string='Phone')
    passport = fields.Char(size=15, string='Passport')
    email = fields.Char(size=15, string='e-mail')
    photo = fields.Binary(string='Photo', filters='*.png,*.gif')
    email_notification = fields.Boolean(string="Receive e-mail notifications")
    can_get_payment = fields.Boolean(string="Can get payment")
    site_notification = fields.Boolean(string="Can get site notifications")
    is_locked = fields.Boolean(string="Accaunt is blocked")
    role = fields.Selection([("admin", "Admin"),("local_admin", "Local admin"), ("User", "User")])

    country = fields.Many2one("rezervation.country", string="Country")
    x = fields.One2many("rezervation.country", "country_id", string="Country")
