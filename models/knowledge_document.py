# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Document(models.Model):
    _name = 'knowledge.document'
    _description = 'Document'

    name = fields.Char('Title', required=True)
    content = fields.Html(string='Content')
    package_id = fields.Many2one(
        'knowledge.package', string='Package', required=True)
    code = fields.Char(string='Code')
    issue_number = fields.Integer(string='Issue Number')
    issue_date = fields.Date(string='Issue Date')
    owner_id = fields.Many2one(
        'res.partner', string='Document Owner', required=True)
    change_item_ids = fields.One2many(
        'knowledge.change.request.item', 'document_id', string='Change History')
    state = fields.Selection(
        string="Status",
        required=True,
        selection=[
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('canceled', 'Canceled')],
        default='draft')
    distribution_list_ids = fields.Many2many(
        'knowledge.distribution.list', string='Distribution lists')
    document_type_id = fields.Many2one(
        'knowledge.document.type', string='Document type', required=True)
