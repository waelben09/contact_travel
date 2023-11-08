from odoo import models, fields, api


# modéle utilisé pour l'heritage des fonctions et classes du modéle contact (res.partner)
class ResPartner(models.Model):
    _inherit = "res.partner"
    #champs relationnel pour recuperer tous les voyage de notre contact courant
    voyages = fields.One2many("contact_travel.voyage", "contact", string="Voyages")
