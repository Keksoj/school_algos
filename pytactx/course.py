import pytactx
from CustomAgent import CustomAgent
import random

agent = CustomAgent("Emmanuel","demo", "demo", "demo", "mqtt.jusdeliens.com")

# Attendre de recevoir le dictionnaire de jeu
while ( len(agent.jeu['destinations']) == 0 ):
  agent.actualiser()

agent.extract_map()
agent.display_destinations()
agent.find_simple_path()
agent.follow_path()
agent.go_to("Versailles")