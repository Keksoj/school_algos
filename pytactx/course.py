import pytactx
import random

agent = pytactx.Agent("hello","demo", "demo", "demo", "mqtt.jusdeliens.com")

agent.actualiser()
destinations = agent.jeu["destinations"]
for ville in destinations.items():
    print(ville)

# to implement
# while (agent.derniereDestinationAtteinte != ville):
    # agent.deplacerVers(ville)
    # agent.actualiser

agent.deplacerVers("Paris")
agent.actualiser()
destinations = agent.jeu["destinations"]
for ville in destinations.items():
    print(ville)
agent.deplacerVers("Versailles")
agent.actualiser()
agent.deplacerVers("Versailles")
agent.actualiser()
agent.deplacerVers("Dreux")
agent.actualiser()
# agent.deplacerVers("Evreux")
# agent.actualiser()
# agent.deplacerVers("Lisieux")
# agent.actualiser()
# agent.deplacerVers("Trouville-sur-Mer")
# agent.actualiser()
# agent.deplacerVers("Pont l'Eveque")
# agent.actualiser()
# agent.deplacerVers("Rouen")
# agent.actualiser()
# agent.deplacerVers("Mantes-la-Jolie")
# agent.actualiser()
# agent.deplacerVers("Paris")
# agent.actualiser()
