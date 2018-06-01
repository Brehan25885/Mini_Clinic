from odoo import models, fields, api


class VisitInheritsfromproduct(models.Model):
    _inherit = "product.template"
    patient_id = fields.Many2one('res.partner')
    price = fields.Float()
    state = fields.Selection([
        ('new', "New"),
        ('invoice', "Invoice"),
        ('done', " Done"),
    ])

    # @api.multi
    # def new(self):
    #     for record in self:
    #         record.state = "new"
    #
    # def invoice(self):
    #     for record in self:
    #         record.state = "invoice"
    #
    # def done(self):
    #     for record in self:
    #         record.state = "done"
    #
