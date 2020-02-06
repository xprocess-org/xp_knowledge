# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Change(models.Model):
    _name = 'knowledge.change.request.item'
    _description = 'Change'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Summary', required=True, index=True)
    content = fields.Html(string='Content')
    change_request_id = fields.Many2one(
        'knowledge.change.request', string='Change request', ondelete='restrict')
    document_id = fields.Many2one(
        'knowledge.document', string='Document')
    document_issue_number = fields.Integer(
        string='Issue Number')
    document_issue_date = fields.Date(string='Issue Date')
    cancel = fields.Boolean(string='Cancel the document')
    state = fields.Selection(
        string="Status",
        required=True,
        selection=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('inprogress', 'In Progress'),
            ('done', 'Done'),
            ('reviewed', 'Reviewed'),
            ('released', 'Released'),
            ('rejected', 'Rejected')],
        default='draft')
    rejection_reason = fields.Text(string='Rejection reason')

    editor_id = fields.Many2one(
        related='document_id.owner_id', string='Editor')
    reviewer_id = fields.Many2one(
        related='document_id.package_id.owner_id', string='Reviewer')
    approver_id = fields.Many2one(
        related='document_id.package_id.approver_id', string='Approver')

    def copy_document(self):
        for item in self:
            item.write({'content': item.document_id.content})
        return True

    def reject_change_item(self):
        for item in self:
            item.write({'state': 'rejected'})
        return True

    def mark_done(self):
        for item in self:
            item.write({'state': 'done'})
        return True

    def mark_not_done(self):
        for item in self:
            item.write({'state': 'inprogress'})
        return True

    def mark_reviewed(self):
        for item in self:
            item.write({'state': 'reviewed'})
        return True

    def release_changes(self):
        for item in self:
            if item.cancel:
                item.write({
                    'state': 'released',
                })
                self.env['knowledge.document'].search([('id', '=', item.document_id.id)]).write({
                    'state': 'canceled',
                })
            else:
                item.write({
                    'state': 'released',
                    'document_issue_number': item.document_id.issue_number + 1,
                    'document_issue_date': fields.Date.today(),
                })
                self.env['knowledge.document'].search([('id', '=', item.document_id.id)]).write({
                    'content': item.content,
                    'issue_number': item.document_issue_number,
                    'issue_date': item.document_issue_date,
                    'state': 'active',
                })
        return True
