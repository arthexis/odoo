from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class EnergySubscriptionRFID(models.Model):
    _name = 'energy.subscription.rfid'
    _description = 'Energy Subscription RFID Card'

    subscription_id = fields.Many2one('energy.subscription', required=True, ondelete='cascade')
    rfid_number = fields.Char(required=True, string='RFID Card Number')

    _sql_constraints = [
        (
            'rfid_number_hex',
            "CHECK (rfid_number ~ '^[0-9A-Fa-f]{8}$')",
            'RFID number must be exactly 8 hexadecimal digits.',
        ),
    ]

    @api.constrains('rfid_number')
    def _check_rfid_number(self):
        hex_re = re.compile(r'^[0-9A-Fa-f]{8}$')
        for rec in self:
            if not hex_re.match(rec.rfid_number or ''):
                raise ValidationError('RFID number must be 8 hex digits (e.g. FFFFFFFF)')
