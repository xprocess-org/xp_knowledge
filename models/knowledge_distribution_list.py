# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class DistributionList(models.Model):
    _name = 'knowledge.distribution.list'
    _description = 'Distribution list'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True)
    partner_ids = fields.Many2many('res.partner', string='Distribution list')
