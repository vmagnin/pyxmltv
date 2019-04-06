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

'''
Surveillance d'un fichier XMLTV contenant les programmes de la TNT pour les
douze prochains jours.
'''

import subprocess
import datetime
import locale
import xml.etree.ElementTree as ET
import argparse
import importlib
import re
import pytz

# Modules du projet :
from telecharger_xmltv import telecharger_xmltv
from enregistrer_xmltv import enregistrer_resultats, string_lien_http

#****************************************************************
# Programme principal
#****************************************************************
SEPARATEUR = "<br />\n" + "_"*80 + "<br /><br />\n"
NAVIGATEUR = "firefox"

# Options de la ligne de commandes :
PARSARG = argparse.ArgumentParser(description="Surveillance d'un fichier XMLTV contenant les programmes de la TNT pour les douze prochains jours", epilog="Sources : <https://github.com/vmagnin/pyxmltv>")
PARSARG.add_argument("-m", action="store", nargs="+",
                     help="Liste de mots-clés ou d'expressions (entre guillemets)", metavar="mot")
PARSARG.add_argument("-f", action="store", nargs=1,
                     help="Fichier .py de mots-clés", metavar="fichier")
PARSARG.add_argument("-q", action="store_true",
                     help="Pas d'affichage (quiet)")
PARSARG.add_argument("-p", action="store_true",
                     help="Affichage uniquement en ligne de commandes (print)")
PARSARG.add_argument("-v", action="version",
                     version="%(prog)s v1.3 Licence GPLv3", help="Version")
ARGS = PARSARG.parse_args()

# Si un fichier de configuration est spécifié, on l'utilise. Sinon si un fichier
# perso_xmltv.py existe on l'utilise, sinon on utilise defaut_xmltv.py :
if ARGS.f is not None:
    try:
        MODU = importlib.import_module(ARGS.f[0])
    except ImportError:
        print("Erreur : fichier de mots-clés introuvable")
        exit(1)

    MOTS_CLES = MODU.MOTS_CLES
    TAGS_A_EXPLORER = MODU.TAGS_A_EXPLORER
    CATEGORIES_A_EVITER = MODU.CATEGORIES_A_EVITER
    CHAINE_RECUES = MODU.CHAINE_RECUES
    SITES_CHAINES = MODU.SITES_CHAINES
else:
    try:
        from perso_xmltv import MOTS_CLES, TAGS_A_EXPLORER, CATEGORIES_A_EVITER, CHAINE_RECUES, SITES_CHAINES
    except ImportError:
        from defaut_xmltv import MOTS_CLES, TAGS_A_EXPLORER, CATEGORIES_A_EVITER, CHAINE_RECUES, SITES_CHAINES

# Sans tous les cas, s'il y a des mots-clés en arguments, c'est eux qu'on utilise :
if ARGS.m is not None:
    MOTS_CLES = ARGS.m

# Nouvelle source (http://allfrtv.ga/xmltv.php) :
#telecharger_xmltv('http://myxmltv.lescigales.org/', 'xmltv.zip')
# On crée l'arbre XML (ElementTree) :
#ARBRE = ET.parse('xmltv.xml')

# Autre source disponible (il faudrait renommer les chaines dans l'autre fichier) :
telecharger_xmltv('http://www.xmltv.fr/guide/', 'tvguide.zip')
# On crée l'arbre XML (ElementTree) :
ARBRE = ET.parse('tvguide.xml')

RACINE = ARBRE.getroot()

# On crée un dictionnaire des chaînes présentes dans le fichier XMLTV :
DICT_CHAINES = {}
for item in RACINE.findall('channel'):
    chaine = item.find('display-name').text
    DICT_CHAINES.update({item.get('id'): chaine})

# Date et heure locales actuelles :
PARIS = pytz.timezone('Europe/Paris')
MAINTENANT = PARIS.localize(datetime.datetime.now())
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')   # Pour l'affichage des dates

# On parcourt l'ensemble des programmes TV :
DICT_RESULTATS = {}
for programme in RACINE.findall('programme'):
    # Est-ce qu'on reçoit cette chaîne ? Sinon on passe au programme suivant...
    if programme.get('channel') not in CHAINE_RECUES:
        continue

    # Première passe : passer au programme suivant si c'est une catégorie à éviter
    eviter = False
    for element in programme.iter():
        if (element.tag == "category") & (element.text in CATEGORIES_A_EVITER):
            eviter = True
            break
    if eviter:
        continue

    # Deuxième passe : passer au programme suivant si pas de mot-clé détecté
    interessant = False
    for element in programme.iter():
        if element.tag in TAGS_A_EXPLORER:
            texte = str(element.text)
            for mot in MOTS_CLES:
                if (texte.find(mot) != -1) or (texte.find(mot.capitalize()) != -1):
                    interessant = True
                    break
            if interessant:
                break
    if not interessant:
        continue

    # Passer au programme suivant s'il est fini :
    fin = programme.attrib['stop']
    date_heure_fin = datetime.datetime.strptime(fin, "%Y%m%d%H%M%S %z")
    if date_heure_fin < MAINTENANT:
        continue

    # Troisième passe : mise en forme pour affichage de cette émission
    chaine = CHAINE_RECUES[programme.attrib['channel']]
    url_chaine = ""
    if chaine in SITES_CHAINES:
        url_chaine = SITES_CHAINES[chaine]
    debut = programme.attrib['start']
    date_heure_debut = datetime.datetime.strptime(debut, "%Y%m%d%H%M%S %z")
    duree = re.search(r'(\d+:\d+):', str(date_heure_fin - date_heure_debut))
    emission = date_heure_debut.strftime("%A %d/%m/%Y de %H:%M à ").capitalize() \
             + date_heure_fin.strftime("%H:%M") \
             + " (" + duree.group(1).replace(":", "h") + ") sur <em>" + chaine \
             + "</em> : " + string_lien_http(url_chaine) + "<br /> \n"

    # On passe en revue les sous-éléments et on formatte le résultat :
    passages_a_la_ligne = 0
    for element in programme.iter():
        texte = str(element.text)
        # Attention, certains éléments peuvent être vides :
        if (texte[0] != "\n") & (texte != "None"):
            if element.tag == "title":
                titre = texte
                texte = "<h2>"+texte+"</h2>\n"
                apres = ""
            elif element.tag == "sub-title":
                texte = "<h3>"+texte+"</h3>\n"
                apres = ""
            elif element.tag == "desc":
                apres = "<br /> \n"
                passages_a_la_ligne += 1
            else:
                apres = " | "

            if (element.tag in ["date", "category"]) & (passages_a_la_ligne == 1):
                avant = "<br /> \n"
                passages_a_la_ligne += 1
            else:
                avant = ""

            if (element.tag == "category") & (texte in ["film", "téléfilm"]):
                texte = '<a href="http://www.allocine.fr/recherche/?q=' + titre.replace(" ", "+") + '">' + texte + '</a>'

            emission = emission + avant + texte + apres

    # On ajoute un séparateur (barre horizontale) entre chaque programme :
    emission = SEPARATEUR + emission

    # On met les mots-clés en gras :
    for mot in MOTS_CLES:
        emission = emission.replace(mot, "<strong>"+mot+"</strong>")
        emission = emission.replace(mot.capitalize(), "<strong>"+mot.capitalize()+"</strong>")

    # On traduit le caractère & de l'HTML :
    emission = emission.replace("%26", "&")

    # La clé "debut" servira au classement chronologique des résultats :
    DICT_RESULTATS.update({debut: emission})

# On enregistre et on affiche les résultats :
enregistrer_resultats(DICT_RESULTATS)

# Si on n'est pas en mode "quiet" (-q) :
if not ARGS.q:
    # Si option -p on affiche dans le terminal, sinon dans le navigateur :
    if ARGS.p:
        for clef in sorted(DICT_RESULTATS):
            print(DICT_RESULTATS[clef])
    else:
        subprocess.Popen([NAVIGATEUR, "tnt.html"])
