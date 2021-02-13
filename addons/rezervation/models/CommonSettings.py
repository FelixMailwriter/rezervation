# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CommonSettings(models.Model):
    _name = 'rezervation.common_settings'
    _description = 'Common settings of reservation systems'

    get_email_on_reservation = fields.Boolean(string='Get e-mail on reservation')
    get_email_on_cancelation = fields.Boolean(string='Get e-mail on cancelation')
    logo = fields.Image(string='Logo')
    send_letter_on_guest_cancellation = fields.Boolean(string='Send letter to guest after cancellation')
    send_letter_on_guest_leaving = fields.Boolean(string='Send letter to guest after leaving')
    days_to_checkin_email_notify = fields.Integer(string='Days to send email before guest arriving')
    days_to_checkin_lc_notify = fields.Integer(string='Days to get guest arriving notification in account')
    agency_name = fields.Char(string='Agency name')
    phone = fields.Char(string='Phone')
    cell_phone = fields.Char(string='Cell phone')
    email = fields.Char(string='E-mail')
    site = fields.Char(string='Site')
    notes = fields.Char(string = 'Notes')
    # currency = fields.One2many("rezervation.currency", "currency_id", string="Currency")
