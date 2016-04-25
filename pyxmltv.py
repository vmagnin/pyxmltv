#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Surveillance d'un fichier XMLTV contenant les programmes de la TNT pour les douze prochains jours. 
./pyxmltv.py -m mot1 mot2 mot3...
Si aucun mot clé n'est fourni, la liste interne au script est utilisée.
Pour chercher une expression, la mettre entre guillemets.
Exemple : ./pyxmltv.py -m "Linus Torvald" Stallman Linux
La casse est prise en compte.
'''

import sys
import zipfile
import os
import subprocess
import datetime
import time
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET
import pytz
import argparse


def telecharger_xmltv(URL_RSS):
    # Nombre de jours depuis l'epoch :
    AUJOURDHUI = int(time.time() / 86400)
    # Date du fichier zip dans le répertoire, s'il est déjà présent :
    JOUR_FICHIER_AVANT = 0
    if os.access("complet.zip", os.F_OK):
        JOUR_FICHIER_AVANT = int(os.stat("complet.zip").st_mtime / 86400)
    # On retélécharge le zip s'il date de plus d'un jour et on extrait le fichier xml :
    if AUJOURDHUI - JOUR_FICHIER_AVANT >= 1:
        FICHIER = urlretrieve(URL_RSS, 'complet.zip')
        ZFILE = zipfile.ZipFile('complet.zip', 'r')
        ZFILE.extractall()
        ZFILE.close()


def enregistrer_resultats(dict_resultats):
    # On enregistre les résultats dans un fichier HTML5 :
    resultats = open("tnt.html", "w")
    resultats.write('<!DOCTYPE html> \n <html> \n <head> <meta charset="UTF-8" /> </head> \n')
    # On met un lien vers un programme TV, ça peut servir :
    resultats.write('<body> <a href="http://television.telerama.fr/tele/grille.php">http://television.telerama.fr/tele/grille.php</a> <br /> <br /> \n')
    # Ecrire les résultats par ordre chronologique (clef) :
    for clef in sorted(dict_resultats):
        resultats.write(dict_resultats[clef])
    # Fin du fichier :
    resultats.write("</body> \n </html> \n")
    resultats.close()

#****************************************************************    
# Programme principal
#****************************************************************    
NAVIGATEUR = "firefox"

# Options de la ligne de commandes :
parsarg = argparse.ArgumentParser(description="Surveillance d'un fichier XMLTV contenant les programmes de la TNT pour les douze prochains jours", epilog="Sources : <https://github.com/vmagnin/pyxmltv>")
parsarg.add_argument("-m", action="store", nargs="+", help="Liste de mots-clés ou d'expressions (entre guillemets)", metavar="mot")
parsarg.add_argument("-q", action="store_true", help="Pas d'affichage (quiet)")
parsarg.add_argument("-p", action="store_true", help="Affichage uniquement en ligne de commandes (print)")
parsarg.add_argument("-v", action="version", version="%(prog)s v0.93 Licence GPLv3", help="Version")
args = parsarg.parse_args()

# S'il n'y a pas de mots-clés en arguments, on utilise la liste (tuple) suivante par défaut :
if len(sys.argv) == 1:
    MOTS_CLES = ("Jude Law", "Star Wars", "La guerre des étoiles", "film d'animation", "téléfilm d'animation", "concert", "Led Zeppelin", "Arvo Pärt", "Bowie", "Björk", "écologie", "Anne Closset", "Yann Arthus-Bertrand", "nucléaire", "film de science-fiction", " astronomie", "chercheur", "brevets", "Snowden", "Linux", "Linus Torvald", "Stallman")
else:
    MOTS_CLES = args.m

TAGS_A_EXPLORER = ("title", "sub-title", "desc", "director", "actor", "composer", "date", "category")

CATEGORIES_A_EVITER = ("série", "série d'animation", "journal", "magazine sportif", "météo", "clips", "téléréalité")

CHAINE_RECUES = {'C1.telerama.fr': 'TF1', 'C2.telerama.fr': 'France 2', 'C3.telerama.fr': 'France 3', 'C112.telerama.fr': 'France 3 Nord Pas-de-Calais', 'C5.telerama.fr': 'France 5', 'C6.telerama.fr': 'M6', 'C7.telerama.fr': 'Arte', 'C8.telerama.fr': 'D8', 'C9.telerama.fr': 'W9', 'C10.telerama.fr': 'TMC', 'C11.telerama.fr': 'NT1', 'C12.telerama.fr': 'NRJ 12', 'C13.telerama.fr': 'France 4', 'C14.telerama.fr': 'La Chaîne Parlementaire', 'C15.telerama.fr': 'BFM TV', 'C16.telerama.fr': 'iTélé', 'C17.telerama.fr': 'D17', 'C18.telerama.fr': 'Gulli', 'C119.telerama.fr': 'France Ô', 'C4131.telerama.fr': 'HD1', 'C4132.telerama.fr': "L'Equipe 21", 'C4133.telerama.fr': '6ter', 'C4134.telerama.fr': 'Numéro 23', 'C4135.telerama.fr': 'RMC Découverte', 'C4136.telerama.fr': 'Chérie 25', 'C133.telerama.fr': 'LCI - La Chaîne Info', 'C87.telerama.fr': 'Euronews', 'C131.telerama.fr': 'La Une', 'C130.telerama.fr': 'La Deux', 'C811.telerama.fr': 'la Trois'}

# Programmes des chaînes de la TNT gratuite, payante et des chaînes locales sur 12 jours :
#telecharger_xmltv('http://kevinpato.free.fr/xmltv/download/tnt.zip')
# Programme de plus de 190 chaînes sur les 12 prochains jours :
telecharger_xmltv('http://kevinpato.free.fr/xmltv/download/complet.zip')

# On crée l'arbre XML (ElementTree) :
ARBRE = ET.parse('complet.xml')
RACINE = ARBRE.getroot()

# On crée un dictionnaire des chaînes présentes dans le fichier XMLTV :
dict_chaines = {}
for item in RACINE.findall('channel'):
    chaine = item.find('display-name').text
    dict_chaines.update({item.get('id'): chaine})

# Date et heure locales actuelles :
PARIS = pytz.timezone('Europe/Paris')
MAINTENANT = PARIS.localize(datetime.datetime.now())

# On parcourt l'ensemble des programmes TV :
dict_resultats = {}
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
                if texte.find(mot) != -1:
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
    debut = programme.attrib['start']
    date_heure_debut = datetime.datetime.strptime(debut, "%Y%m%d%H%M%S %z")
    emission = date_heure_debut.strftime("%A %d/%m/%Y de %H:%M à ") + date_heure_fin.strftime("%H:%M") + " sur <em>" + chaine + "</em> <br /> \n"
    # On passe en revue les sous-éléments et on formatte le résultat :
    passages_a_la_ligne = 0
    for element in programme.iter():
        texte = str(element.text)
        # Attention, certains éléments peuvent être vides :
        if (texte[0] != "\n") & (texte != "None"):
            if element.tag == "title":
                texte = "<h2>"+texte+"</h2>\n"
                apres = " "
            elif element.tag == "sub-title":
                texte = "<h3>"+texte+"</h3>\n"
                apres = " "
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

            emission = emission + avant + texte + apres

    # On ajoute un séparateur (barre horizontale) entre chaque programme :
    emission = "\n <hr /> \n" + emission
    # On met les mots-clés en gras :
    for mot in MOTS_CLES:
        emission = emission.replace(mot, "<strong>"+mot+"</strong>")
            
    # La clé "debut" servira au classement chronologique des résultats :
    dict_resultats.update({debut: emission})

# On enregistre et on affiche les résultats :
enregistrer_resultats(dict_resultats)

if not args.q:
    if args.p:
        for clef in sorted(dict_resultats):
            print(dict_resultats[clef])
    else:
        subprocess.Popen([NAVIGATEUR, "tnt.html"])
