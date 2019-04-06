#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Fonction pour enregistrer les émissions intéressantes
'''

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
