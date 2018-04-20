# -*- coding: utf-8 -*-

from odoo import fields, api, models, _

class ProductTemplate(models.Model):
	"""docstring for ProductTemplate"""
	_inherit = 'product.template'

	code = fields.Char(string="Code")