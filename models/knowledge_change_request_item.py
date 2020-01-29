# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Change(models.Model):
    _name = 'knowledge.change.request.item'
    _description = 'Change'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Summary', required=True)
    content = fields.Html(string='Content')
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

    editor_id = fields.Many2one('res.partner', string='Editor')
    reviewer_id = fields.Many2one('res.partner', string='Reviewer')
    approver_id = fields.Many2one('res.partner', string='Approver')
