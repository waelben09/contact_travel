# -*- coding: utf-8 -*-
{
    'name': "contact_travel",


    'description': """
        Le module "contact_travel" permet de gérer efficacement les voyages, de suivre le nombre de voyages par utilisateur,
         et d'attribuer des niveaux de récompense en fonction des voyages effectués. 
         Il améliore la gestion des clients et des voyages dans Odoo, 
         offrant des fonctionnalités de suivi et de récompense pour les utilisateurs.
    """,

    'author': "wael benkherfallah",
    'website': "https://github.com/waelben09/contact_travel",


    'category': 'Uncategorized',
    'version': '0.1',

    # Modules dont dépend le bon fonctionnement de celui-ci.
    'depends': ['base', 'contacts'],

    # Données qui seront toujours chargées avec ce module.
    'data': [
        'security/ir.model.access.csv',  # Fichier de sécurité pour la gestion des autorisations d'accès.
        'views/voyage_view.xml',  # Vues associées au modèle 'Voyage'.
        'views/destination_view.xml',  # Vues associées au modèle 'Destination'.
        'views/contact_inherit.xml',  # Vue qui étend et modifie la vue du modèle 'Contact'.
        'views/menu.xml',  # Fichier pour la création de menus dans l'interface Odoo.
    ],

    # Données utilisées uniquement en mode de démonstration.
    'demo': [
        'demo/demo.xml',  # Données de démonstration, telles que des exemples d'enregistrements.
    ],

    # Indique si le module peut être installé.
    'installable': True,

    # Indique si le module est une application (utile pour le référencement dans l'interface Odoo).
    'application': True,

    # Séquence de chargement du module:
    # le sequence 0 permet d'afficher mon module contact_travel en premiere position dans la liste des applications.
    'sequence': 0,

}
