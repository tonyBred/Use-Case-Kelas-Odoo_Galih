from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Kelas(models.Model):
    _name = 'kelas.kelas'

    name = fields.Char(string='Nama Kelas')
    partner_id = fields.One2many(
        comodel_name='res.partner',
        inverse_name='kelas_id',
        string='Mahasiswa',
    )
    wali_kelas = fields.Many2one(
        comodel_name='res.partner',
        string="Wali Kelas",
        domain=[
            ("is_dosen", "=", True),
        ],
    )
    matkul_ids = fields.Many2many(
        comodel_name='mata.kuliah', 
        string='Mata Kuliah'
    )
    
    