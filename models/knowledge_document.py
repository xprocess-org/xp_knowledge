# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Document(models.Model):
    _name = 'knowledge.document'
    _description = 'Document'

    name = fields.Char('Title', required=True)
    package_id = fields.Many2one(
        'knowledge.package', string='Package', required=True)
    code = fields.Char(string='Code')
    issue_number = fields.Integer(string='Issue Number', required=True)
    issue_date = fields.Date(string='Issue Date', required=True)
    owner_id = fields.Many2one(
        'res.partner', string='Document Owner', required=True)
    section_ids = fields.One2many(
        'knowledge.section', 'document_id', string='Sections')
