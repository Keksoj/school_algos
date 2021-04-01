
# voisins =
# {'Max T.':
#  {'x': 3,
#   'y': 10,
#   'orientation': 0,
#   'munitions': 10,
#   'distance': 0,
#   'vie': 100,
#   'tir': False,
#   'couleur': [60, 60, 60],
#   'derniereDestinationAtteinte': ''
#   }
#  }
# fonction d'évaluation de proximité et niveau de vie des voisins
# compléter un dictionnaire de voisin
# itérer le dictionnaire pour trouver le plus faible
# trouver l'enchaînement de coups minimal pour le tuer
import time
import pytactx
import random
import math

agent = pytactx.Agent("Plop", "demo",
                      "demo", "demo", "mqtt.jusdeliens.com")


def eval(agent, voisin):
    """
    Évalue la difficulté de tuer un agent voisin
    """
    ecart_x = abs(agent.x - voisin['x'])
    ecart_y = abs(agent.y - voisin['y'])
    distance = math.sqrt(ecart_x * ecart_x + ecart_y * ecart_y)
    difficulte = voisin['vie'] + 3 * distance
    voisin['difficulte'] = difficulte


while agent.vie > 0:

    # récupérer le dictionnaire des voisins:
    dico_de_voisins = agent.voisins
    agent.actualiser()

    # parcourir le dictionnaire de voisins pour évaluer chaque agent
    for voisin in dico_de_voisins.values():
        print(type(voisin))
        eval(agent, voisin)

    # parcourir le dictionnaire de voisins pour trouver le moins difficile à tuer
    difficulte_min = 1000
    for key, voisin in dico_de_voisins.items():
        print(
            "\rdifficulté du voisin",
            key,
            voisin['difficulte']
        )
        if (voisin['difficulte'] < difficulte_min):
            difficulte_min = voisin['difficulte']

    print("\ndifficulté mininum:", difficulte_min)
    time.sleep(1)

# todo: aller à la position du voisin le plus proche
