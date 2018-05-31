from odoo import models, fields


class Visit(models.Model):
    _name = "clinic.visit"
    patient_id = fields.Many2one('clinic.patient',
                                    ondelete='set null', string="Patient", index=True)
    price = fields.Float()
    state = fields.Selection([
        ('new', "New"),
        ('inv', " Inv"),
        ('done', " Done"),
    ])

