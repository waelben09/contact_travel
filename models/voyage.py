# modéle principale du module voyage

from odoo import models, fields , api


class Voyage(models.Model):
    _name = "contact_travel.voyage"
    _description = "Voyage"

    # Nom du voyage
    name = fields.Char(string="Voyage", required=True)
    # Champ de relation Many2one avec le modèle "res.partner" pour lier un client à cet enregistrement.
    contact = fields.Many2one("res.partner", string="Client")
    # date de départ
    departure_date = fields.Date(string="Departure Date")
    # destination
    destination = fields.Many2one("contact_travel.destination")

