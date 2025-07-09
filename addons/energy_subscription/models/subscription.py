from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class EnergySubscription(models.Model):
    _name = 'energy.subscription'
    _description = 'Energy Subscription'

    name = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    kwh_balance = fields.Float(string='kWh Balance', default=0.0)
    period_months = fields.Integer(string='Review Period (months)', default=1)
    next_review_date = fields.Date(string='Next Review Date')
    rfid_ids = fields.One2many('energy.subscription.rfid', 'subscription_id', string='RFID Cards')
    vin_ids = fields.One2many('energy.subscription.vin', 'subscription_id', string='VINs')
    allow_overcharge = fields.Boolean(string='Allow Overcharge', default=False)

    def credit_kwh(self, amount):
        for sub in self:
            sub.kwh_balance += amount
        return True

    def debit_kwh(self, amount):
        for sub in self:
            new_balance = sub.kwh_balance - amount
            if new_balance < 0 and not sub.allow_overcharge:
                raise ValidationError(
                    _('Subscription %s cannot be overcharged') % sub.display_name
                )
            sub.kwh_balance = new_balance
        return True

    @api.model
    def _cron_generate_bills(self):
        today = fields.Date.context_today(self)
        subs = self.search([('next_review_date', '<=', today)])
        for sub in subs:
            self.env['energy.bill'].create({
                'subscription_id': sub.id,
                'amount_kwh': sub.kwh_balance,
            })
            sub.next_review_date = fields.Date.add(today, months=sub.period_months)
