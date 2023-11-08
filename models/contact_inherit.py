from odoo import models, fields, api


# modéle utilisé pour l'heritage des fonctions et classes du modéle contact (res.partner)
class ResPartner(models.Model):
    _inherit = "res.partner"
    #champs relationnel pour recuperer tous les voyage de notre contact courant
    voyages = fields.One2many("contact_travel.voyage", "contact", string="Voyages")
    #compteur de nombre de voyage dans le champs précédent
    voyages_count = fields.Integer(compute="get_voyages_length")
    # champs affichant le niveau de récompense
    reward_level = fields.Selection([
            ("silver", "Argent"),
            ("gold", "Or"),
            ("platinum", "Platine"),
            ("nf", "Non definie"),
        ],
        compute="_compute_reward_level",
        string="Niveau de récompense",)


    # champs affichant le prix total des voyages d'un utilisateur
    total_price = fields.Float("Montant totale des voyage", compute="total_amount_computer")



    # fonction qui permet de rediriger l'utilisateur vers la liste des voyage de contact (client) courant
    def open_voyage_form_view(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "contact_travel.action_voyage_tree"
        )
        action["domain"] = [("contact.id", "=", self.id)]
        return action

    # fonction qui permet de calculé le nombre total de voyages éffectués par un utilisateur
    def get_voyages_length(self):
        for rec in self:
            if rec.voyages:
                rec.voyages_count = len(rec.voyages)
            else:
                rec.voyages_count = len(rec.voyages)

    # fonction qui permet le calcule du montant total des voyages éffectués par un utilisateur
    def total_amount_computer(self):
        for rec in self:
            total_price = 0.0
            if rec.voyages:
                for voyage in rec.voyages:
                    total_price += voyage.price
                rec.total_price = total_price
            else:
                rec.total_price = 0.0

    # fonction d'affectation automatique du niveau de récompense client par rapport au montant total de ses voyages
    @api.depends("total_price")
    def _compute_reward_level(self):
        for rec in self:
            if rec.total_price:
                if rec.total_price >= 200000:
                    rec.reward_level = "platinum"
                elif rec.total_price >= 100000:
                    rec.reward_level = "gold"
                elif rec.total_price >= 50000:
                    rec.reward_level = "silver"
                else:
                    rec.reward_level = "nf"
            else:
                rec.reward_level = False


