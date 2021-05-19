# pytactx

Jeu en python faite par [Julien Arné](http://jusdeliens.com), on le trouve ici: <http://jusdeliens.com/play/pytactx/> ("demo", "demo" comme identifiants, et "découvrir PytactX")

C'est une lib (`pytactx.py`) qui permet de se connecter au jeu en mqtt, d'instancier un agent,
de lui définir un comportement pour qu'il dézingue les autres agents.

## pré-requis

Avoir `pip-python` pour installer `paho-mqtt`.

## Machine à états

    python machine_a_etats.py

Selon les états du programme, appeles des fonctions qui définissent des comportements.
On est soit dans un état, soit dans un autre.

## Trouver le voisin le plus proche avec le dictionnaire

    python voisins.py

La propriété `voisin` de la classe `Pytactx.Agent` renvoie un dictionnaire du genre

    {
        'Terminator':
            {
                'x': 3,
                'y': 10,
                'orientation': 0,
                'munitions': 10,
                'distance': 0,
                'vie': 100,
                'tir': False,
                'couleur': [60, 60, 60],
                'derniereDestinationAtteinte': ''
            }
        // et d'autres valeurs
    }

et on doit s'en servir pour trouver le voisin le plus vulnérable.

## La course Pytactx

    python course.py

[L'arène](https://jusdeliens.com/play/pytactx/)
a changé apparemment. Ce n'est plus un damier mais un graphe de villes.


