import pytactx
import random


# class MonAgent(pytactx.Agent):
#     def __init__(self, nom, truc, machin, bidule, mqtt_serveur):
#         pytactx.Agent.__init__(self, nom, truc, machin, bidule, mqtt_serveur)

#     def bouger_vers(self, x, y):
#         while self.x != x or self.y != y:
#             self.deplacer(x, y)
#             self.actualiser()


def random_coordinates():
    random_x = random.randint(0, 10)
    random_y = random.randint(0, 10)
    return (random_x, random_y)


agent = pytactx.Agent("emmanuel_", "demo",
                      "demo", "demo", "mqtt.jusdeliens.com")
# smith = MonAgent("smith", "demo", "demo", "demo", "mqtt.jusdeliens.com")

etat = "recherche"
objectif = random_coordinates()


def rechercher():
    global etat
    if (agent.distance == 0):
        bouger(objectif)
    else:
        agent.tirer(True)
        etat = "poursuite"


def poursuivre():
    global etat
    if (agent.distance > 0):
        agent.tirer(True)
    else:
        agent.tirer(False)
        etat = "recherche"


def bouger(objectif):
    # global objectif
    print("objectif:", objectif)
    agent.deplacer(objectif[0], objectif[1])
    if (agent.x == objectif[0] and agent.y == objectif[1]):
        objectif = random_coordinates()
        bouger(objectif)


while agent.vie > 0:
    if (etat == "recherche"):
        rechercher()
    elif (etat == "poursuite"):
        poursuivre()
    agent.actualiser()

# orientation = 0
# while smith.vie > 0:
#     smith.orienter(orientation)

#     if (orientation > 0):
#         orientation = 0

#     smith.deplacer(0, 10)
#     smith.actualiser()

#     orientation += 1


# goto(smith, 0, 5)
# goto(smith, 0, 10)
# goto(smith, 10, 10)
# goto(smith, 10, 0)
