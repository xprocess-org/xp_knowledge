# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class DocumentType(models.Model):
    _name = 'knowledge.document.type'
    _description = 'Document type'

    name = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    code = fields.Boolean(string='Has a code', help="the document has a code")
    issue = fields.Boolean(
        string='Controlled', help="the document has a issue number and issue date")
    external_document = fields.Boolean(
        string='External Document', help="the document is an external file")
    template = fields.Many2one(
        'knowledge.document.template', string='Preferred template', help="the preferred template in case it's internal document")
