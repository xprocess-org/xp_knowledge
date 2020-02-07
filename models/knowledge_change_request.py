# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ChangeRequest(models.Model):
    _name = 'knowledge.change.request'
    _description = 'Change request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "priority desc, sequence, id desc"

    name = fields.Char('Title', required=True, index=True)
    description = fields.Html('Details')
    change_item_ids = fields.One2many(
        'knowledge.change.request.item', 'change_request_id', string='Change Items')
    package_id = fields.Many2one(
        'knowledge.package', string='Package', required=True, ondelete='restrict')
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
        group_expand='_expand_states',
        copy=False,
        help='Status of the change request',
        default='draft'
    )
    rejection_reason = fields.Text(string='Rejection reason')
    color = fields.Integer()
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Important'),
    ], default='0', index=True, string="Priority")
    sequence = fields.Integer(string='Sequence', index=True, default=10,
                              help="Gives the sequence order when displaying a list of requests.")

    def submit_change_request(self):
        for request in self:
            request.write({'state': 'submitted'})
            for change_item in request.change_item_ids:
                change_item.write({'state': 'submitted'})
        return True

    def approve_change_request(self):
        for request in self:
            request.write({'state': 'approved'})
        return True

    def reject_change_request(self):
        for request in self:
            request.write({'state': 'rejected'})
            for change_item in request.change_item_ids:
                change_item.write({'state': 'rejected'})
        return True

    def open_change_request(self):
        for request in self:
            request.write({'state': 'open'})
            for change_item in request.change_item_ids:
                change_item.write({'state': 'inprogress'})
        return True

    def close_change_request(self):
        for request in self:
            request.write({'state': 'closed'})
        return True

    def reopen_change_request(self):
        for request in self:
            request.write({'state': 'open'})
        return True

    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]

    def write(self, values):
        if 'state' in values:
            previous_state = self.state
            new_state = values.get('state')
            if (new_state in ['approved', 'open', 'closed', 'rejected']) and (self.package_id.owner_id != self.env.user):
                raise ValidationError(
                    _("Only Package Manager can perform that move"))
            elif (new_state == 'closed'):
                for item in self.change_item_ids:
                    if item.state != 'released':
                        raise ValidationError(
                            _("All change items need to be released before closing the request"))
        return super(ChangeRequest, self).write(values)
