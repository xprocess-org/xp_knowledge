# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class DocumentType(models.Model):
    _name = 'knowledge.document.type'
    _description = 'Document type'

    name = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
