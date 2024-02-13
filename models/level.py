from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError
from datetime import *
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


class level_level(models.Model):
    _name = 'level.level'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'Represents level object and data'

    name = fields.Char(string='Level')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    students_ids = fields.Many2many('student.student', string='Students')
    material_lines = fields.One2many('material.material', 'level_id', string='Materials')

    def action_view_material(self):
        material_lines = self.mapped('material_lines')
        domain = [('id', 'in', material_lines.ids)]
        context = {
            'default_level_id': self.id,
        }
        return {
            'name': _('material_lines'),
            'res_model': 'material.material',
            'view_mode': 'tree,form',
            'domain': domain,
            'context': context,
            'type': 'ir.actions.act_window',
        }


# class material_material(models.Model):
#     _name = 'material.material'
#     _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
#     _description = 'Represents material object and data'
#
#     name = fields.Char(string='Material Name')
#     basic_teacher = fields.Many2one('teacher.teacher')
#     level_id = fields.Many2one('level.level')


