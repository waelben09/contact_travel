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
    # Champ de relation Many2one avec le modèle "res.currency" pour lier la devise choisis .
    currency_id = fields.Many2one("res.currency", string="Currency",compute="get_currency")
    price = fields.Monetary(string="Prix")

    # Définition d'une méthode onchange dans Odoo qui se déclenche lorsque le champ 'contact' est modifié.
    @api.onchange('contact')
    def get_currency(self):
        for rec in self:
            # Vérification si un contact est sélectionné.
            if rec.contact:
                # Si un contact est sélectionné, met à jour 'currency_id' avec la devise du contact.
                rec.currency_id = rec.contact.currency_id
            else:
                # Si aucun contact n'est sélectionné, défini 'currency_id' comme False.
                rec.currency_id = False

