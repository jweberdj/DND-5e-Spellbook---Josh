###########################
##  D&D Spellbook, 5e
##  Joshua Weber
##  
##  -- TO DOs --
##  * 
##  
##
##
##
###########################

import requests
import json
from spellbook import Spellbook

run = True
response = requests.get('http://dnd5eapi.co/api/spells').json()['results']
sb = Spellbook(input('What would you like to name your spellbook?\n'), response)

while run:
    spell = input("\nCurrently looking at '{}', the spellbook.\nWhat spell are you trying to find?\n\nType 'exit' to leave this program.\n\n".format(sb.name))
    if spell.lower() == 'exit':
        run = False
        continue
    else:
        sb.readSpell(spell)
        print('\n\n')






