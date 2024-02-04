from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError
from datetime import *
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    birthdate = fields.Datetime(string="Birth Date", help="Birth Date", config_parameter="school_ms.birthdate")


