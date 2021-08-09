from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True,
        )
    kelas_id = fields.Many2one(
        comodel_name='kelas.kelas',
        string='Kelas',
    )
    is_dosen = fields.Boolean(string='Check Dosen ?')

    birth_date = fields.Date(string='Tanggal Lahir', default=fields.Date.today())

    @api.depends('birth_date')
    def _compute_age(self):
        if self.birth_date == date.today():
            self.age = 0
        else:
            now = date.today()
            delta = now - self.birth_date
            self.age = delta.days / 365
    
    @api.constrains('birth_date')
    def _check_birth_date(self):
        if self.birth_date > date.today():
            raise models.ValidationError('Birth date must be in the past') 