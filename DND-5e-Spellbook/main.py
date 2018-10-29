import requests
import json
from spellbook import Spellbook

response = requests.get('http://dnd5eapi.co/api/spells').json()['results']
#print(response)

sb = Spellbook('My Book', response)


sb.readSpell(sb.findSpell('magic missile'))

