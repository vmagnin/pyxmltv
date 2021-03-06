# pyxmltv v1.7

Script Python 3 sous licence GNU GPL v3 permettant de surveiller des fichiers au
format XMLTV contenant les programmes de la TNT française pour les prochains
jours. Les fichiers XMLTV sont récupérés à ces adresses :

* Source 1 (par défaut) : https://xmltv.ch/xmltv/xmltv-tnt.zip
* Source 2 : semble ne plus être disponible...


## Utilisation

```
usage: pyxmltv.py [-h] [-m mot [mot ...]] [-f fichier] [-s source] [-q] [-p]
                  [-v]

optional arguments:
  -h, --help        show this help message and exit
  -m mot [mot ...]  Liste de mots-clés ou d'expressions (entre guillemets)
  -f fichier        Fichier .py de mots-clés
  -s source         Source du fichier XMLTV : 1 (défaut) ou 2
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
* L'affichage se fait dans le navigateur par défaut.

## Définir vos fichiers perso

### fichier `perso_xmltv.py`

Votre fichier `perso_xmltv.py` contiendra vos propres listes et dictionnaires,
sur le même modèle que `defaut_xmltv.py` :

```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    MOTS_CLES = ("film d'animation", "Linus Torvald", "Stallman")
    TAGS_A_EXPLORER = ("title", "category")
    CATEGORIES_A_EVITER = ("série", "téléréalité")
```

Il ne sera pas inclus dans le dépôt GitHub, ce qui permet de découpler le
développement du script et l'utilisation personnelle. Vous pourrez utiliser
d'autres fichiers sur le même modèle avec l'option `-f`.

### fichier `perso_chaines_xmltv.py`

Idem pour le fichier `perso_chaines_xmltv.py` dans lequel vous placerez la liste
des chaînes que vous recevez, avec leurs identifiants et leurs URL :

```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    CHAINE_RECUES = {'C1.telerama.fr': 'TF1', 'C2.telerama.fr': 'France 2'}
    SITES_CHAINES = {'Arte': 'http://www.arte.tv/guide/fr'}
```

En son absence, c'est `defaut_xmltv.py` qui sera utilisé.

Si vous utilisez plusieurs sources, plusieurs identifiants peuvent correspondre
à la même chaîne, ces identifiants n'étant pas normalisés. Dans ce cas, vous
pouvez sans problème inclure ces différents identifiants dans le même
dictionnaire.

## Divers

Le téléchargement de l'ETag présent dans l'en-tête HTTP et sa conservation
permettent de s'assurer que le fichier volumineux a été mis à jour avant
de le télécharger. S'il n'y a pas d'ETag, on utilise si possible le champ
Last-Modified.


Vincent MAGNIN, 3 mars 2020
