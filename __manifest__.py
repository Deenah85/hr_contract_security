{
    'name': 'HR Contract Access Control',
    'version': '1.0',
    'summary': 'Control access to contracts and payslips based on HR security groups',
    'category': 'Human Resources',
    'author': 'Dina Sarhan',
    'depends': ['hr_contract', 'hr_payroll_community'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_contract_access_rules.xml',
        'views/hr_contract_views.xml',
        'views/hr_payslip_views.xml',
    ],
    'installable': True,
    'application': False,
}