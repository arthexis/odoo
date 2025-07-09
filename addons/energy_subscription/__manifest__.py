{
    'name': 'Energy Subscription',
    'version': '0.1',
    'summary': 'Manage customer energy subscriptions',
    'description': """Manage energy credits for customers with periodic billing.
Customers purchase kWh that can be manually or automatically refilled.
Credit and debit operations are available through the standard API.""",
    'author': 'My Company',
    'category': 'Services',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/energy_subscription_menu.xml',
        'views/energy_subscription_views.xml',
        'views/energy_subscription_wizard.xml',
        'report/bill_report.xml',
        'data/cron.xml',
    ],
    'installable': True,
    'application': True,
}
