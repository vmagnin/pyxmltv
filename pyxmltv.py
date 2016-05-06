#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Surveillance d'un fichier XMLTV contenant les programmes de la TNT pour les
douze prochains jours.
'''

import zipfile
import os
import subprocess
import datetime
from urllib.request import urlretrieve, urlopen, URLError
import xml.etree.ElementTree as ET
import argparse
import importlib
import re
import pickle
import pytz


def telecharger_xmltv(url, nom_fichier):
    """
    Télécharge le fichier situé à url si une nouvelle version est disponible
    """
    # On récupère l'ETag HTTP du fichier déjà éventuellement
    # présent dans le répertoire du script :
    try:
        with open("ETag_xmltv.pickle", 'rb') as FICHIER_ETag:
            ANCIEN_ETag = pickle.load(FICHIER_ETag)
    except OSError:
        ANCIEN_ETag = "0"

    # On récupère l'ETag HTTP du zip sur le serveur :
    try:
        entete = urlopen(url+nom_fichier).info()
        match = re.search(r'ETag: "(\w+-\w+-\w+)"', str(entete))
        ETag = match.group(1)
    except URLError:
        ETag = "00"

    # On retélécharge le zip s'il a été modifié sur le serveur:
    if ETag != ANCIEN_ETag:
        try:
            urlretrieve(url+nom_fichier, nom_fichier)
            with zipfile.ZipFile(nom_fichier, 'r') as zfile:
                zfile.extractall()
                # On sauvegarde l'ETag du fichier zip :
                with open("ETag_xmltv.pickle", 'wb') as FICHIER_ETag:
                    pickle.dump(ETag, FICHIER_ETag)
        except URLError:
            print("Attention ! Téléchargement nouveau fichier impossible...")
            if not os.access(nom_fichier, os.F_OK):
                print("Erreur : pas de fichier dans le répertoire courant !")
                exit(2)


def string_lien_http(url):
    """
    Renvoie sous forme de chaine un lien http codé en HTML
    """
    return '<a href="' + url + '">' + url + '</a>'


def enregistrer_resultats(dico_resultats):
    """
    Enregistre les résultats par ordre chronologique dans un fichier HTML5
    """
    with open("tnt.html", "w") as resultats:
        resultats.write('<!DOCTYPE html>\n<html>\n<head><meta charset="UTF-8" /></head>\n')
        # On met un lien vers un programme TV, ça peut servir :
        lien = 'http://television.telerama.fr/tele/grille.php'
        resultats.write('<body> ' + string_lien_http(lien) + '<br /><br />\n')
        # Ecrire les résultats par ordre chronologique (cle) :
        for cle in sorted(dico_resultats):
            resultats.write(dico_resultats[cle])
        # Fin du fichier :
        resultats.write("</body> \n </html> \n")

#****************************************************************
# Programme principal
#****************************************************************
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
                     version="%(prog)s v1.0 Licence GPLv3", help="Version")
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

# Programme de plus de 190 chaînes sur les 12 prochains jours :
telecharger_xmltv('http://kevinpato.free.fr/xmltv/download/', 'complet.zip')
# On crée l'arbre XML (ElementTree) :
ARBRE = ET.parse('complet.xml')
RACINE = ARBRE.getroot()

# On crée un dictionnaire des chaînes présentes dans le fichier XMLTV :
DICT_CHAINES = {}
for item in RACINE.findall('channel'):
    chaine = item.find('display-name').text
    DICT_CHAINES.update({item.get('id'): chaine})

# Date et heure locales actuelles :
PARIS = pytz.timezone('Europe/Paris')
MAINTENANT = PARIS.localize(datetime.datetime.now())

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
    url_chaine = ""
    if chaine in SITES_CHAINES:
        url_chaine = SITES_CHAINES[chaine]
    debut = programme.attrib['start']
    date_heure_debut = datetime.datetime.strptime(debut, "%Y%m%d%H%M%S %z")
    emission = date_heure_debut.strftime("%A %d/%m/%Y de %H:%M à ") \
             + date_heure_fin.strftime("%H:%M") + " sur <em>" + chaine \
             + "</em> : " + string_lien_http(url_chaine) + "<br /> \n"
    # On passe en revue les sous-éléments et on formatte le résultat :
    passages_a_la_ligne = 0
    for element in programme.iter():
        texte = str(element.text)
        # Attention, certains éléments peuvent être vides :
        if (texte[0] != "\n") & (texte != "None"):
            if element.tag == "title":
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

            emission = emission + avant + texte + apres

    # On ajoute un séparateur (barre horizontale) entre chaque programme :
    emission = "\n <br /><hr /><br />\n" + emission
    # On met les mots-clés en gras :
    for mot in MOTS_CLES:
        emission = emission.replace(mot, "<strong>"+mot+"</strong>")
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
