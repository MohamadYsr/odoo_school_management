# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError
from datetime import *
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Student_student(models.Model):
    _name = 'student.student'
    _description = 'This model represent a student object'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    name = fields.Char(string="Name", copy=False, tracking=True)
    age = fields.Integer(string="Age", copy=False, tracking=True, compute="compute_age", store=True)

    def _default_birthdate(self):
        birthdate = self.env['ir.config_parameter'].sudo().get_param('school_ms.birthdate')
        return birthdate

    birthdate = fields.Date(string="Birth Date", copy=False, tracking=True, default=_default_birthdate)
    note = fields.Text(string="Note", tracking=True)

    image_1000 = fields.Binary()

    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancelled')], default='draft'
    )
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], tracking=True
    )

    basic_teacher = fields.Many2one('teacher.teacher', string="Basic Teacher")

    grade = fields.Selection(
        [('1', 'Grade 1'),('2', 'Grade 2'),('3', 'Grade 3')], string='Grade'
    )

    active = fields.Boolean(default=True)

    code = fields.Char(string="Number", required="True", copy="False",
                       default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('code', _('New')) == _('New'):
                vals['code'] = self.env['ir.sequence'].next_by_code('sequence.student' or _('New'))
        return super().create(vals_list)

    @api.onchange('grade')
    def onchange_grade(self):
        for record in self:
            if record.grade:
                return {'domain': {'basic_teacher': [('grade', '=', record.grade)]}}

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age < 7 or record.age > 17:
                raise ValidationError(
                    _("The age of the student must be between 7 and 15 years old")
                )

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name must be unique !')
    ]

    @api.depends('birthdate')
    def compute_age(self):
        for record in self:
            if record.birthdate:
                d1 = datetime.strptime(str(record.birthdate), "%Y-%m-%d").date()
                d2 = datetime.today()

                record.age = relativedelta(d2, d1).years
            else:
                record.age = 0

    def action_done(self):
        self.state = 'done'
        self.active = True

    def action_draft(self):
        self.state = 'draft'
        self.active = True

    def action_cancel(self):
        self.state = 'cancel'
        self.active = False


# class Teacher(models.Model):
#     _name = 'teacher.teacher'
#     _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
#     _description = 'Represents a teacher object and data'
#
#     name = fields.Char(string="Teacher Name", required=True)
#     age = fields.Integer(string="Teacher Age", copy=False, tracking=True, compute="compute_age", store=True)
#     birthdate = fields.Date(string="Birth Date", copy=False)
#
#     gender = fields.Selection(
#         [('male', 'Male'), ('female', 'Female')], string="Teacher Gender"
#     )
#
#     note = fields.Text(string="Teacher Note", copy=False)
#
#     state = fields.Selection(
#         [('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancelled')], default='draft'
#     )
#
#     grade = fields.Selection(
#         [('1', 'Grade 1'), ('2', 'Grade 2'), ('3', 'Grade 3')], string='Grade'
#     )
#
#     contact_id = fields.Many2one('res.partner')
#
#     active = fields.Boolean(default=True)
#
#     @api.constrains('age')
#     def _check_age(self):
#         for records in self:
#             if records.age < 22:
#                 raise ValidationError(
#                     _("The age of the teacher must be above 22 years old")
#                 )
#
#     _sql_constraints = [
#         ('name_uniq', 'unique(name)', 'The name must be unique !')
#     ]
#
#     def action_done(self):
#         self.state = 'done'
#         self.active = True
#
#     def action_draft(self):
#         self.state = 'draft'
#         self.active = True
#
#     def action_cancel(self):
#         self.state = 'cancel'
#         self.active = False
#
#     @api.depends('birthdate')
#     def compute_age(self):
#         for record in self:
#             if record.birthdate:
#                 d1 = datetime.strptime(str(record.birthdate), "%Y-%m-%d").date()
#                 d2 = datetime.today()
#
#                 record.age = relativedelta(d2, d1).years
#             else:
#                 record.age = 0


# class school_ms(models.Model):
#     _name = 'school_ms.school_ms'
#     _description = 'school_ms.school_ms'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
