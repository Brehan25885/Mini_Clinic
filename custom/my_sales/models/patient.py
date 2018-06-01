from odoo import models,fields, api


class patientInheritsCustomer(models.Model):
    _inherit = "res.partner"
    #test=fields.Char();
    visits_ids=fields.One2many('product.template','patient_id')