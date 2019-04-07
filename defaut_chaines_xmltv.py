#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce fichier par défaut contient une liste des chaînes reçues, avec leur identifiant
dans le fichier XMLTV, ainsi que les URL de leurs sites web. Il est commité dans
GitHub.
Vous pouvez créer sur le même modèle votre fichier perso_chaines_xmltv.py. Le
script pyxmltv.py l'utilisera et se rabattera sur le fichier default_chaines_xmltv.py
s'il n'existe pas.
"""

CHAINE_RECUES = {'C192.api.telerama.fr': 'TF1',
                 'C4.api.telerama.fr': 'France 2',
                 'C80.api.telerama.fr': 'France 3',
                 'C47.api.telerama.fr': 'France 5',
                 'C118.api.telerama.fr': 'M6',
                 'C111.api.telerama.fr': 'Arte',
                 'C445.api.telerama.fr': 'C8',
                 'C119.api.telerama.fr': 'W9',
                 'C195.api.telerama.fr': 'TMC',
                 'C446.api.telerama.fr': 'NT1',
                 'C444.api.telerama.fr': 'NRJ 12',
                 'C78.api.telerama.fr': 'France 4',
                 'C234.api.telerama.fr': 'La Chaîne Parlementaire',
                 'C481.api.telerama.fr': 'BFM TV',
                 'C226.api.telerama.fr': 'CNews (i>Télé)',
                 'C458.api.telerama.fr': 'CStar (D17)',
                 'C482.api.telerama.fr': 'Gulli',
                 'C160.api.telerama.fr': 'France Ô',
                 'C1404.api.telerama.fr': 'HD1',
                 'C1401.api.telerama.fr': "L'Equipe 21",
                 'C1403.api.telerama.fr': '6ter',
                 'C1402.api.telerama.fr': 'Numéro 23',
                 'C1400.api.telerama.fr': 'RMC Découverte',
                 'C1399.api.telerama.fr': 'Chérie 25',
                 'C112.api.telerama.fr': 'LCI - La Chaîne Info',
                 'C2111.api.telerama.fr': 'France Info',
                }

SITES_CHAINES = {'TF1': 'http://www.tf1.fr/grille-tv',
                 'France 2': 'http://www.france2.fr/programme-tv',
                 'France 3': 'http://www.france3.fr/programme-tv',
                 'France 5': 'http://www.france5.fr/programme-tv',
                 'M6': 'http://www.m6.fr/grille_des_programmes.html',
                 'Arte': 'http://www.arte.tv/guide/fr',
                 'C8': 'http://guide.mycanal.fr/guide-tv/grille-tv/pid642-grille-tv-chaine.html?epgid=450',
                 'W9': 'http://www.w9.fr/grille_des_programmes.html',
                 'TMC': 'http://www.tf1.fr/grille-tv',
                 'NT1': 'http://www.tf1.fr/grille-tv',
                 'NRJ 12': 'http://www.nrj12.fr/grille-tv-4186/programmetv/grille/',
                 'France 4': 'http://www.france4.fr/programme-tv',
                 'La Chaîne Parlementaire': 'http://www.lcp.fr/programmes',
                 'BFM TV': 'http://www.bfmtv.com/emission/',
                 'CNews (i>Télé)': 'http://www.cnews.fr/grille',
                 'CStar (D17)': 'http://guide.mycanal.fr/guide-tv/grille-tv/pid642-grille-tv-chaine.html?epgid=513',
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
