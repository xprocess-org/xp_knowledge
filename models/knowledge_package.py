# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Package(models.Model):
    _name = 'knowledge.package'
    _description = 'Package'

    name = fields.Char('Title', required=True)
    description = fields.Html(string='Description')
    owner_id = fields.Many2one(
        'res.users', string='Package Manager', default=lambda self: self.env.uid, ondelete='restrict', required=True)
    approver_id = fields.Many2one(
        'res.users', string='Package Approver', default=lambda self: self.env.uid, ondelete='restrict', required=True)
    visibility = fields.Selection([
        ('followers', 'Distribution list'),
        ('employees', 'All employees'),
        ('portal', 'Portal users and all employees')
    ], string='Visibility')
    document_ids = fields.One2many(
        'knowledge.document', 'package_id', string='Documents')
    request_ids = fields.One2many(
        'knowledge.change.request', 'package_id', string='Requests')
    color = fields.Integer('Color Index')
