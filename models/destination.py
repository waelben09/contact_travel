from odoo import models, fields

#Création d'un modèle de destinations pour simplifier la gestion et éviter la saisie répétitive lors de la création de voyages.
#IL S'AGIT D'UN MODELE SUPPLEMENTAIRE NON MENTIONNER DANS LE TEST
class Destination(models.Model):
    _name = "contact_travel.destination"  # Nom du modèle dans Odoo.
    _description = "Destinations"  # Description du modèle.

    # Champ de texte pour le nom de la destination, obligatoire.
    name = fields.Char(string="Nom", required=True)

    # Champ de texte pour la description de la destination.
    description = fields.Char(string="Desciption")