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
    issue_number = fields.Integer(string='Issue Number', default=1)
    issue_date = fields.Date(string='Issue Date', required=True)
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
