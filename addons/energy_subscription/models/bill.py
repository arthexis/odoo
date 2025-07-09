from odoo import models, fields


class EnergyBill(models.Model):
    _name = 'energy.bill'
    _description = 'Energy Bill'

    subscription_id = fields.Many2one('energy.subscription', required=True, ondelete='cascade')
    partner_id = fields.Many2one(related='subscription_id.partner_id', store=True)
    date = fields.Date(default=fields.Date.context_today)
    amount_kwh = fields.Float(string='kWh Amount')
