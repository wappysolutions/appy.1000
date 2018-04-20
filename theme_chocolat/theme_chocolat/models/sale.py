# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class SaleOrder(models.Model):
	"""docstring for SaleOrder"""
	_inherit = 'sale.order'

	@api.multi
	def action_command_confirm_sent(self):
		""" Open a window to compose an email, with the edi invoice template
				message loaded by default
		"""
		self.ensure_one()
		template = self.env.ref('theme_chocolat.choco_email_template_sale_order_confirm', False)
		compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
		ctx = dict(
			default_model='sale.order',
			default_res_id=self.id,
			default_use_template=bool(template),
			default_template_id=template and template.id or False,
			default_composition_mode='comment',
			mark_invoice_as_sent=True,
			custom_layout="theme_chocolat.choco_mail_template_data_notification_email_sale_order_confirm"
		)
		return {
			'name': _('Order confirmation - Send by mail'),
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form.id, 'form')],
			'view_id': compose_form.id,
			'target': 'new',
			'context': ctx,
		}

	@api.multi
	def action_quotation_send(self):
		'''
		This function opens a window to compose an email, with the edi sale template message loaded by default
		'''
		self.ensure_one()
		ir_model_data = self.env['ir.model.data']
		try:
			template_id = ir_model_data.get_object_reference('sale', 'email_template_edi_sale')[1]
		except ValueError:
			template_id = False
		try:
			compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
		except ValueError:
			compose_form_id = False
		ctx = dict()
		ctx.update({
			'default_model': 'sale.order',
			'default_res_id': self.ids[0],
			'default_use_template': bool(template_id),
			'default_template_id': template_id,
			'default_composition_mode': 'comment',
			'mark_so_as_sent': True,
			'custom_layout': "theme_chocolat.choco_mail_template_data_notification_email_sale_order"
		})
		return {
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form_id, 'form')],
			'view_id': compose_form_id,
			'target': 'new',
			'context': ctx,
		}