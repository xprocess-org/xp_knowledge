# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Package(models.Model):
    _name = 'knowledge.package'
    _description = 'Package'

    name = fields.Char('Title', required=True)
