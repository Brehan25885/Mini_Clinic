from odoo import models, fields, api


class Visit(models.Model):
    _name = "clinic.visit"
    patient_id = fields.Many2one('clinic.patient',
                                    ondelete='set null', string="Patient", index=True)
    price = fields.Float()
    state = fields.Selection([
        ('new', "New"),
        ('invoice', "Invoice"),
        ('done', " Done"),
    ])

    @api.multi
    def new(self):
        for record in self:
            record.state = "new"

    def invoice(self):
        for record in self:
            record.state = "invoice"

    def done(self):
        for record in self:
            record.state = "done"

