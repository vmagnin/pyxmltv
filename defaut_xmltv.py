#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Vincent MAGNIN, 2016-2019

"""
Tuples et dictionnaire utilisés par défaut s'il n'y a pas
de fichier perso_xmltv.py dans le répertoire
"""

MOTS_CLES = ("Jude Law", "Star Wars", "La guerre des étoiles",
                "film d'animation", "téléfilm d'animation", "pop %26 rock",
                "Led Zeppelin", "Arvo Pärt", "Bowie", "Björk", "écologie",
                "Anne Closset", "Yann Arthus-Bertrand", "nucléaire",
                "film de science-fiction", " astronomie", "chercheur",
                "brevets",
                "Snowden", "Linux", "Linus Torvald", "Stallman")

TAGS_A_EXPLORER = ("title", "sub-title", "desc", "director", "actor",
                    "composer", "date", "category")

CATEGORIES_A_EVITER = ("série", "série d'animation", "journal", 
                       "magazine sportif", "météo", "clips", "Clips", "téléréalité", "téléfilm de science-fiction", "sport", "Sport", "Série TV", "Série Télé", "Téléréalité")

CHAINE_RECUES = {'TF1.fr': 'TF1', 
                'France2.fr': 'France 2', 
                'France3.fr': 'France 3', 
                'France3Nord-PasDeCalais.fr': 'France 3 Nord Pas-de-Calais', 
                'France5': 'France 5', 
                'M6.fr': 'M6', 
                'Arte.fr': 'Arte', 
                'C8.fr': 'C8', 
                'W9.fr': 'W9', 
                'TMC.fr': 'TMC', 
                'NT1.fr': 'NT1', 
                'NRJ12.fr': 'NRJ 12', 
                'France4.fr': 'France 4', 
                'LCP.fr': 'La Chaîne Parlementaire', 
                'BFMTV.fr': 'BFM TV', 
                'CNews.fr': 'CNews (i>Télé)', 
                'CStar.fr': 'CStar (D17)', 
                'Gulli.fr': 'Gulli', 
                'FranceO.fr': 'France Ô', 
                'HD1.fr': 'HD1', 
                "EquipeTV.fr": "L'Equipe 21", 
                '6ter.fr': '6ter', 
                'Numero23.fr': 'Numéro 23', 
                'RMCdecouverte.fr': 'RMC Découverte', 
                'Cherie25.fr': 'Chérie 25', 
                'LCI': 'LCI - La Chaîne Info', 
                #'C509.telerama.fr': 'Ketnet',  # Pas dispos dans cette source
                # Canvas
                #'C81.telerama.fr' : 'één', 
                'EuronewsF': 'Euronews', 
                'LaUne.be': 'La Une', 
                'LaDeux.be': 'La Deux', 
                'LaTrois.be': 'La Trois'}

# Ancienne source : http://kevinpato.free.fr/xmltv/download/
#CHAINE_RECUES = {'C1.telerama.fr': 'TF1', 
                #'C2.telerama.fr': 'France 2', 
                #'C3.telerama.fr': 'France 3',
                #'C5.telerama.fr': 'France 5', 
                #'C6.telerama.fr': 'M6', 
                #'C7.telerama.fr': 'Arte', 
                #'C8.telerama.fr': 'D8', 
                #'C9.telerama.fr': 'W9', 
                #'C10.telerama.fr': 'TMC', 
                #'C11.telerama.fr': 'NT1', 
                #'C12.telerama.fr': 'NRJ 12', 
                #'C13.telerama.fr': 'France 4', 
                #'C14.telerama.fr': 'La Chaîne Parlementaire', 
                #'C15.telerama.fr': 'BFM TV', 
                #'C16.telerama.fr': 'iTélé', 
                #'C17.telerama.fr': 'D17', 
                #'C18.telerama.fr': 'Gulli', 
                #'C119.telerama.fr': 'France Ô', 
                #'C4131.telerama.fr': 'HD1', 
                #'C4132.telerama.fr': "L'Equipe 21", 
                #'C4133.telerama.fr': '6ter', 
                #'C4134.telerama.fr': 'Numéro 23', 
                #'C4135.telerama.fr': 'RMC Découverte', 
                #'C4136.telerama.fr': 'Chérie 25', 
                #'C133.telerama.fr': 'LCI - La Chaîne Info',
                #'C87.telerama.fr': 'Euronews', 
                #'C131.telerama.fr': 'La Une', 
                #'C130.telerama.fr': 'La Deux', 
                #'C811.telerama.fr': 'la Trois'}

SITES_CHAINES = {'TF1': 'http://www.tf1.fr/grille-tv',
                 'France 2': 'http://www.france2.fr/programme-tv',
                 'France 3': 'http://www.france3.fr/programme-tv',
                 'France 5': 'http://www.france5.fr/programme-tv',
                 'M6': 'http://www.m6.fr/grille_des_programmes.html',
                 'Arte': 'http://www.arte.tv/guide/fr',
                 'D8': 'http://www.d8.tv/pid5227-d8-grille-tv.html',
                 'W9': 'http://www.w9.fr/grille_des_programmes.html',
                 'TMC': 'http://www.tf1.fr/grille-tv',
                 'NT1': 'http://www.tf1.fr/grille-tv',
                 'NRJ 12': 'http://www.nrj12.fr/grille-tv-4186/programmetv/grille/',
                 'France 4': 'http://www.france4.fr/programme-tv',
                 'La Chaîne Parlementaire': 'http://www.lcp.fr/programmes',
                 'BFM TV': 'http://www.bfmtv.com/emission/',
                 'CNews (i>Télé)': 'http://www.itele.fr/grille',
                 'CStar (D17)': 'http://www.d17.tv/pid5228-d17-grille-tv.html',
                 'Gulli': 'http://www.gulli.fr/programme-tv',
                 'France Ô': 'http://www.franceo.fr/programme-tv',
                 'HD1': 'http://www.tf1.fr/grille-tv',
                 "L'Equipe 21": 'http://www.lequipe.fr/lequipe21/grille',
                 '6ter': 'http://www.6ter.fr/guide-tv.html',
                 'Numéro 23': 'http://www.numero23.fr/guide-tv/',
                 'RMC Découverte': 'http://rmcdecouverte.bfmtv.com/grille-programme-tv/',
                 'Chérie 25': 'http://www.cherie25.fr/grille-tv-4271/programmetv/grille/',
                 'LCI - La Chaîne Info': 'http://lci.tf1pro.com/lcipro/grille/',
                 'Euronews': 'http://fr.euronews.com/programmes/',
                 'La Une': 'http://www.rtbf.be/tv/laune/guide-tv',
                 'La Deux': 'http://www.rtbf.be/tv/ladeux/guide-tv',
                 'La Trois': 'http://www.rtbf.be/tv/latrois/guide-tv'}
