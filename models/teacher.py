from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError
from datetime import *
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Teacher(models.Model):
    _name = 'teacher.teacher'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'Represents a teacher object and data'

    name = fields.Char(string="Teacher Name", required=True)
    age = fields.Integer(string="Teacher Age", copy=False, tracking=True, compute="compute_age", store=True)
    birthdate = fields.Date(string="Birth Date", copy=False)

    image = fields.Binary()

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Teacher Gender"
    )

    note = fields.Text(string="Teacher Note", copy=False)

    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancelled')], default='draft'
    )

    grade = fields.Selection(
        [('1', 'Grade 1'), ('2', 'Grade 2'), ('3', 'Grade 3')], string='Grade'
    )

    contact_id = fields.Many2one('res.partner')

    active = fields.Boolean(default=True)

    @api.constrains('age')
    def _check_age(self):
        for records in self:
            if records.age < 22:
                raise ValidationError(
                    _("The age of the teacher must be above 22 years old")
                )

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name must be unique !')
    ]

    def action_done(self):
        self.state = 'done'
        self.active = True

    def action_draft(self):
        self.state = 'draft'
        self.active = True

    def action_cancel(self):
        self.state = 'cancel'
        self.active = False

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {}, name=_("%s (copy)", self.name))
        return super(Teacher, self).copy(default=default)

    @api.depends('birthdate')
    def compute_age(self):
        for record in self:
            if record.birthdate:
                d1 = datetime.strptime(str(record.birthdate), "%Y-%m-%d").date()
                d2 = datetime.today()

                record.age = relativedelta(d2, d1).years
            else:
                record.age = 0
