from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MataKuliah(models.Model):
    _name = 'mata.kuliah'

    name = fields.Char(string='Name')
    kode = fields.Char(string='Kode')
    kelas_ids = fields.Many2many(
        comodel_name='kelas.kelas', 
        string='Kelas',
        readonly=True,
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Dosen Pengampu',
        domain=[
            ("is_dosen", "=", True),
        ],
    )
    