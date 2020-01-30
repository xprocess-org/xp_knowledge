# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class DocumentType(models.Model):
    _name = 'knowledge.document.type'
    _description = 'Document type'

    name = fields.Char(string='Title', required=True)
    template = fields.Html(string='Template')
    code = fields.Boolean(string='Has a code', help="the document has a code")
    issue = fields.Boolean(
        string='Controlled', help="the document has a issue number and issue date")
    external_document = fields.Boolean(
        string='External Document', help="the document is an external file")
