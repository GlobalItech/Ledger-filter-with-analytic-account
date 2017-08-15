# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountingReport(models.TransientModel):
    _inherit = "accounting.report"
    _description = "Accounting Report"
    
    analytical_ids=fields.Many2many("account.analytic.account",string="Analytic Account")
    
    def _print_report(self, data):
        data['form'].update(self.read(['date_from_cmp', 'debit_credit', 'date_to_cmp', 'filter_cmp', 'account_report_id','analytical_ids', 'enable_filter', 'label_filter', 'target_move'])[0])
        return self.env['report'].get_action(self, 'account.report_financial', data=data)
#         data = self.pre_print_report(data)
#         data['form'].update({'account_ids': self.account_ids.ids,})
#         return super(AccountReportGeneralLedger, self)._print_report(data)