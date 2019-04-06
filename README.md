# pyxmltv v1.5

Script Python 3 sous licence GNU GPL v3 permettant de surveiller un fichier au
format XMLTV contenant les programmes de la TNT française pour les prochains
jours. Le fichier XMLTV est récupéré à cette adresse :
http://www.xmltv.fr/guide/


## Utilisation

```
usage: pyxmltv.py [-h] [-m mot [mot ...]] [-f fichier] [-q] [-p] [-v]

optional arguments:
  -h, --help        show this help message and exit
  -m mot [mot ...]  Liste de mots-clés ou d'expressions (entre guillemets)
  -f fichier        Fichier .py de mots-clés
  -q                Ne lance pas le navigateur (quiet)
  -p                Affichage uniquement en ligne de commandes (print)
  -v                Version
```

* Priorités d'utilisation des mots-clés :
    1. mots-clés fournis par l'option `-m`,
    2. fichier de mots-clés spécifié par `-f`,
    3. fichier `perso_xmltv.py`,
    4. fichier `defaut_xmltv.py` en dernier recours.
* Pour chercher une expression, la mettre entre guillemets, par exemple :
    `./pyxmltv.py -m "Linus Torvald" Stallman Linux`
* La casse des mots-clés est prise en compte.


## Définir votre fichier perso

Votre fichier `perso_xmltv.py` contiendra vos propres listes et dictionnaires,
sur le même modèle que `defaut_xmltv.py` :

```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    MOTS_CLES = ("film d'animation", "Linus Torvald", "Stallman")
    TAGS_A_EXPLORER = ("title", "category")
    CATEGORIES_A_EVITER = ("série", "téléréalité")
    CHAINE_RECUES = {'C1.telerama.fr': 'TF1', 'C2.telerama.fr': 'France 2'}
    SITES_CHAINES = {'Arte': 'http://www.arte.tv/guide/fr'}
```

Il ne sera pas inclus dans le dépôt GitHub, ce qui permet de découpler le 
développement du script et l'utilisation personnelle. Vous pourrez utiliser 
d'autres fichiers sur le même modèle avec l'option `-f`.


## Divers

Le téléchargement de l'ETag présent dans l'en-tête HTTP et sa conservation
permettent de s'assurer que le fichier volumineux a été mis à jour avant
de le télécharger. S'il n'y a pas d'ETag, on utilise si possible le champ
Last-Modified.


Vincent MAGNIN, 6 avril 2019
