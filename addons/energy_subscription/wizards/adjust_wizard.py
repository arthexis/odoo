from odoo import models, fields


class EnergySubscriptionAdjustWizard(models.TransientModel):
    _name = 'energy.subscription.adjust.wizard'
    _description = 'Adjust Energy Subscription Balance'

    subscription_id = fields.Many2one('energy.subscription', required=True)
    amount = fields.Float(required=True)
    operation = fields.Selection([
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ], required=True, default='credit')

    def action_apply(self):
        self.ensure_one()
        if self.operation == 'credit':
            self.subscription_id.credit_kwh(self.amount)
        else:
            self.subscription_id.debit_kwh(self.amount)
        return {'type': 'ir.actions.act_window_close'}
