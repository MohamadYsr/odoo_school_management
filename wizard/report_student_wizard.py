from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError
from datetime import *
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


class wizard_report_student(models.TransientModel):
    _name = 'wizard.report.student'
    show_all_grades = fields.Boolean(default=True)
    grade = fields.Selection(
        [('1', 'Grade 1'), ('2', 'Grade 2'), ('3', 'Grade 3')], string='Grade'
    )

    def print_report_pdf(self):
        [data] = self.read()
        datas = {
            'ids': [],
            'model': 'student.student',
            'form': data
        }
        return self.env.ref('school_ms.student_details_report').report_action([], data=datas)

    def print_report_xlsx(self):
        data = {
            'form_data': self.read()[0],
        }
        return self.env.ref('school_ms.student_details_xlsx').report_action([], data=data)
