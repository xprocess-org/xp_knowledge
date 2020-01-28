# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Change(models.Model):
    _name = 'knowledge.change.request.item'
    _description = 'Change'

    name = fields.Char('Summary', required=True)
    change_request_id = fields.Many2one(
        'knowledge.change.request', string='Change request')
    document_id = fields.Many2one(
        'knowledge.document', string='Document')
    document_issue_number = fields.Integer(
        string='Issue Number')
    document_issue_date = fields.Date(string='Issue Date')
    state = fields.Selection(
        string="Status",
        required=True,
        selection=[
            ('draft', 'Draft'),
            ('inprogress', 'In Progress'),
            ('done', 'Done'),
            ('reviewed', 'Reviewed'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected')],
        default='draft')
    rejection_reason = fields.Text(string='Rejection reason')
