from odoo import models, fields


class EnergySubscriptionVIN(models.Model):
    _name = 'energy.subscription.vin'
    _description = 'Energy Subscription VIN'

    subscription_id = fields.Many2one('energy.subscription', required=True, ondelete='cascade')
    vin = fields.Char(required=True, string='Vehicle VIN')
