from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError
from datetime import *
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

class material_material(models.Model):
    _name = 'material.material'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'Represents material object and data'

    name = fields.Char(string='Material Name')
    basic_teacher = fields.Many2one('teacher.teacher')
    level_id = fields.Many2one('level.level')
    active = fields.Boolean(default=True)
