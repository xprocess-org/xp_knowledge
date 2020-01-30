# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Document(models.Model):
    _name = 'knowledge.document'
    _description = 'Document'
    _sql_constraints = [
        ('knowledge_document_name_package_uq',  # Constraint unique identifier
         'UNIQUE (name, package_id)',  # Constraint SQL syntax
         'Document title must be unique in each package.'),  # Message
    ]

    name = fields.Char('Title', required=True)
    content = fields.Html(string='Content')
    package_id = fields.Many2one(
        'knowledge.package', string='Package', required=True)
    code = fields.Char(string='Code')
    issue_number = fields.Integer(string='Issue Number')
    issue_date = fields.Date(string='Issue Date')
    owner_id = fields.Many2one(
        'res.partner', string='Document Owner', required=True)
    change_item_ids = fields.One2many(
        'knowledge.change.request.item', 'document_id', string='Change History')
    state = fields.Selection(
        string="Status",
        required=True,
        selection=[
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('canceled', 'Canceled')],
        default='draft')
    distribution_list_ids = fields.Many2many(
        'knowledge.distribution.list', string='Distribution lists')
    document_type_id = fields.Many2one(
        'knowledge.document.type', string='Document type', required=True)
    external_document = fields.Binary(string='External Document')
    related_documents = fields.Many2many(
        'knowledge.document',
        'knowledge_document_knowledge_document_rel',
        'id1',
        'id2',
        'Related Documents')

    # document type fields
    has_code = fields.Boolean(related='document_type_id.code', store=True)
    has_issue = fields.Boolean(related='document_type_id.issue', store=True)
    has_external_document = fields.Boolean(
        related='document_type_id.external_document', store=True)
    template = fields.Html(related='document_type_id.template', store=True)

    def apply_template(self):
        for document in self:
            document.write({'content': document.template})
        return True
