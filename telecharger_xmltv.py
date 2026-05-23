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

# Vincent MAGNIN, 2016-2026
# Dernière modification : 23-05-2026

'''
Fonction pour télécharger un fichier XMLTV
'''

import zipfile
import os
import re
import pickle
from urllib.request import urlretrieve, urlopen, URLError, Request


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

    # Nécessaire avec les sites refusant les requêtes par Python :
    requete = Request(
        url=url + nom_fichier,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    # On récupère l'ETag HTTP du zip sur le serveur :
    try:
        entete = urlopen(requete).info()
        match = re.search(r'ETag: "(\w+-\w+-\w+)"', str(entete))
        ETag = match.group(1)
    except URLError:
        ETag = "00"
        print("URL erronée")
    except AttributeError:  # Si match est vide (pas de ETag disponible)
        ETag = "00"
        # On essaie d'utiliser à la place le champ Last-Modified
        try:
            entete = urlopen(requete).info()
            match = re.search(r'Last-Modified: (.*)', str(entete))
            ETag = match.group(1)
        except AttributeError:
            ANCIEN_ETag = "0"    # On force le téléchargement du zip

    # On re-télécharge le zip s'il a été modifié sur le serveur:
    if ETag != ANCIEN_ETag:
        print("Chargement de la dernière version en ligne...")
        try:
            with urlopen(requete) as reponse, open(nom_fichier, 'wb') as f:
                f.write(reponse.read())
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
