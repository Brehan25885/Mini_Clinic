from odoo import models, fields


class Patient(models.Model):
    _name = "clinic.patient"

    name = fields.Char()
    mobile= fields.Char()
    visits_ids=fields.One2many('clinic.visit','visit_id')