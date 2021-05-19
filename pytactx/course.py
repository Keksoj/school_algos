import pytactx
from CustomAgent import CustomAgent
import random

agent = CustomAgent("Emmanuel","demo", "demo", "demo", "mqtt.jusdeliens.com")

agent.actualiser()

agent.display_destinations()
agent.go_to("Versailles")