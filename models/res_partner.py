from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, timedelta

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(
        string='Umur',
        compute='_compute_age',
        inverse="_inverse_age",
        search='_search_age',
        store=False,
        compute_sudo=True
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
            delta = date.today() - self.birth_date
            self.age = delta.days / 365


    def _inverse_age(self):
        today = fields.Date.today()
        for book in self.filtered('birth_date'):
            d = today - timedelta(days=book.self.age*365)
            book.birth_date = d

    def _search_age(self, operator, value):
        today = fields.Date.today()
        value_days = timedelta(days=value)
        value_date = today - value_days
        # convert the operator:
        # book with age > value have a date < value_date
        operator_map = {
            '>': '<', '>=': '<=',
            '<': '>', '<=': '>=',
            }
        new_op = operator_map.get(operator, operator)
        return [('date_release', new_op, value_date)]


    @api.constrains('birth_date')
    def _check_birth_date(self):
        if self.birth_date > date.today():
            raise models.ValidationError('Birth date must be in the past')