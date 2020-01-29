# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class DocumentTemplate(models.Model):
    _name = 'knowledge.document.template'
    _description = 'Document template'

    name = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
