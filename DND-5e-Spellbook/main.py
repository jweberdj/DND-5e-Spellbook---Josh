import requests
import json
from spellbook import Spellbook
from random import randint

run = True
sb = Spellbook()

while run:
    spell = input("\nWhat spell are you trying to find?\n\nType 'exit' to leave this program or 'restart' to restart the progarm.\n\n")
    if spell.lower() == 'exit':
        run = False
        print('Good luck adventurer!')
        continue
    elif spell.lower() == 'restart':
        print('RESTARTING...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        continue
    elif spell.lower() == 'rolld20' or spell.lower() == 'roll d20':
        print("------------------------------\n----- You rolled a {} -----\n------------------------------".format(randint(1,20)))

    else:
        print('\n--------------------------\n')
        sb.readSpell(spell)
        print('\n\n')



