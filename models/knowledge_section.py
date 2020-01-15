# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Section(models.Model):
    _name = 'knowledge.section'
    _description = 'Section'

    name = fields.Char('Title', required=True)
