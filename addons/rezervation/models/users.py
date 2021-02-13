# -*- coding: utf-8 -*-

from odoo import models, fields, api


class user(models.Model):
    _name = 'user.rezervation'
    _description = 'User for reservation systems'

    login = fields.Char(size=30, string='login', required=True)
    password = fields.Char(size=30, string='password', required=True)
    email = fields.Char(size=30, string='e-mail', required=True)
    date_registration = fields.Datetime(string='Date of registration')
    phone = fields.Char(size=15, string='phone')
    first_name = fields.Char(size=15, string='First name', required=True)
    last_name = fields.Char(size=15, string='Last name', required=True)
    role = fields.Char(size=15, string='Role', required=True)
    is_locked = fields.Boolean(string='Is locked')
    email_notification_required = fields.Boolean(string='E-mail notification required')
    can_get_payment = fields.Boolean(string='Can get payment')
    site_notification_requirement = fields.Boolean(string='Site notification requirement')
    gender = fields.Selection([
       ('male', 'Male'),
       ('female', 'Female'),
    ], string='Gender', deefault='male')
    # user_type_ids = fields.Many2many("Rezervation.user_types", on_delete='cascade', string="User types")





#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100