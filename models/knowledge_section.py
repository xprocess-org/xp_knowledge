# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Section(models.Model):
    _name = 'knowledge.section'
    _description = 'Section'

    name = fields.Char('Title', required=True)
    content = fields.Html('Section content', required=True)
    active = fields.Boolean(string='Active')
    version = fields.Integer('Version', default=1, required=True)
    change_summary = fields.Char('Change summary', required=True)
    change_request_id = fields.Many2one(
        'knowledge.change.request', string='Change request')
    document_id = fields.Many2one(
        'knowledge.document', string='Document')
