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
    document_count = fields.Integer(
        compute='_compute_document_count', string='Document count')
    request_count = fields.Integer(
        compute='_compute_request_count', string='Request count')

    def _compute_document_count(self):
        document_data = self.env['knowledge.document'].read_group(
            [('package_id', 'in', self.ids)], ['package_id'], ['package_id'])
        result = dict((data['package_id'][0], data['package_id_count'])
                      for data in document_data)
        for document in self:
            document.document_count = result.get(document.id, 0)

    def _compute_request_count(self):
        request_data = self.env['knowledge.change.request'].read_group(
            [('package_id', 'in', self.ids)], ['package_id'], ['package_id'])
        result = dict((data['package_id'][0], data['package_id_count'])
                      for data in request_data)
        for request in self:
            request.request_count = result.get(request.id, 0)
