# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ChangeRequest(models.Model):
    _name = 'knowledge.change.request'
    _description = 'Change request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Title', required=True)
    description = fields.Html('Details')
    change_item_ids = fields.One2many(
        'knowledge.change.request.item', 'change_request_id', string='Change Items')
    package_id = fields.Many2one(
        'knowledge.package', string='Package', required=True)
    state = fields.Selection(
        string="Status",
        required=True,
        selection=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
            ('open', 'Open'),
            ('closed', 'Closed'),
            ('rejected', 'Rejected')],
        default='draft')
    rejection_reason = fields.Text(string='Rejection reason')

    def submit_change_request(self):
        for request in self:
            request.write({'state': 'submitted'})
        return True

    def approve_change_request(self):
        for request in self:
            request.write({'state': 'approved'})
        return True

    def reject_change_request(self):
        for request in self:
            request.write({'state': 'rejected'})
        return True

    def open_change_request(self):
        for request in self:
            request.write({'state': 'open'})
        return True

    def close_change_request(self):
        for request in self:
            request.write({'state': 'closed'})
        return True

    def reopen_change_request(self):
        for request in self:
            request.write({'state': 'open'})
        return True
