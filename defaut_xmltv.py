#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
                        "magazine sportif", "météo", "clips",
                        "téléréalité")

CHAINE_RECUES = {'C1.telerama.fr': 'TF1',
                    'C2.telerama.fr': 'France 2',
                    'C3.telerama.fr': 'France 3',
                    'C112.telerama.fr': 'France 3 Nord Pas-de-Calais',
                    'C5.telerama.fr': 'France 5',
                    'C6.telerama.fr': 'M6',
                    'C7.telerama.fr': 'Arte',
                    'C8.telerama.fr': 'D8',
                    'C9.telerama.fr': 'W9',
                    'C10.telerama.fr': 'TMC',
                    'C11.telerama.fr': 'NT1',
                    'C12.telerama.fr': 'NRJ 12',
                    'C13.telerama.fr': 'France 4',
                    'C14.telerama.fr': 'La Chaîne Parlementaire',
                    'C15.telerama.fr': 'BFM TV',
                    'C16.telerama.fr': 'iTélé',
                    'C17.telerama.fr': 'D17',
                    'C18.telerama.fr': 'Gulli',
                    'C119.telerama.fr': 'France Ô',
                    'C4131.telerama.fr': 'HD1',
                    'C4132.telerama.fr': "L'Equipe 21",
                    'C4133.telerama.fr': '6ter',
                    'C4134.telerama.fr': 'Numéro 23',
                    'C4135.telerama.fr': 'RMC Découverte',
                    'C4136.telerama.fr': 'Chérie 25',
                    'C133.telerama.fr': 'LCI - La Chaîne Info',
                    'C87.telerama.fr': 'Euronews',
                    'C131.telerama.fr': 'La Une',
                    'C130.telerama.fr': 'La Deux',
                    'C811.telerama.fr': 'la Trois'}

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
                 'iTélé': 'http://www.itele.fr/grille',
                 'D17': 'http://www.d17.tv/pid5228-d17-grille-tv.html',
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
                 'la Trois': 'http://www.rtbf.be/tv/latrois/guide-tv'}
