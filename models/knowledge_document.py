# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Document(models.Model):
    _name = 'knowledge.document'
    _description = 'Document'

    name = fields.Char('Title', required=True)
