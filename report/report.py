from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError


class ReportStudentDetails(models.AbstractModel):
    _name = 'report.school_ms.report_studentdetails'
    _description = 'Student Details'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data['form'].get('grade', False):
            students = self.env['student.student'].search([('grade', '=', data['form'].get('grade', False))])
            return {
                'students': students,
                'data': data['form'],
            }
        else:
            students = self.env['student.student'].search([])
            return {
                'students': students,
                'data': data['form'],
            }


class PartnerXlsx(models.AbstractModel):
    _name = 'report.school_ms.student_details_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        