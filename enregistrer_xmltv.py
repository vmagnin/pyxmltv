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
