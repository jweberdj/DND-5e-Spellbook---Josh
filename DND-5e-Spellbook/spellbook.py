import requests
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Spellbook(object):
        def __init__(self):
                self.spells = requests.get('http://dnd5eapi.co/api/spells').json()['results']

        def printSpell(self, spelldata):
                components = ''
                for p in spelldata['components']:
                        components += ' {}'.format(p)
                print('\n----------------------\n- Spell Name: {}\n-----------------\n'.format(spelldata['name']))
                print('- Description: {}\n'.format(spelldata['desc'][0]))
                try:
                        print('- At a Higher Level: {}\n'.format(spelldata['higher_level'][0]))
                except KeyError:
                        print('- Higher Level: N/A\n')
                print('- Page: {}\n'.format(spelldata['page']))
                print('- Range: {}\n'.format(spelldata['range']))
                print('- Components: {}\n'.format(components))
                try:
                        print('- Material: {}\n'.format(spelldata['material']))
                except KeyError:
                        print('- Material: N/A\n')
                print('- Ritual: {}\n'.format(spelldata['ritual']))
                print('- Duration: {}\n'.format(spelldata['duration']))
                print('- Concentration: {}\n'.format(spelldata['concentration']))
                print('- Casting Time: {}\n'.format(spelldata['casting_time']))
                print('- Casting Level: {}\n'.format(spelldata['level']))
                print('- Magic School: {}\n------------------------------------'.format(spelldata['school']['name']))

        def spellSearch(self, spell):
                rs = [x[0]['name'] for x in process.extract(spell, self.spells)[0:3]]
                return rs
                
        def readSpell(self, spell):
                # input: str
                found = False
                for x in self.spells:
                        if x['name'].lower() == spell.lower():
                                self.printSpell(requests.get(x['url']).json())
                                found = True
                                break
                        else:
                                pass
                if not found:
                        print("We could not find a match. These options may be close:\n")
                        count = 0
                        inputerror = True
                        qresults = self.spellSearch(spell)
                        for num,r in enumerate(qresults, start=1):
                                print("{}. {}\n".format(num, r))
                        
                        uinput = int(input("Type the option that best matches your search or type '-r' to restart your search.\n\n"))
                        while inputerror:
                                try:
                                        if uinput in range(len(qresults)+1):
                                                self.readSpell(qresults[uinput-1])
                                                inputerror = False
                                        elif uinput == '-r':
                                                inputerror = False
                                                pass
                                        else:
                                                uinput = input("Sorry, that's not an option!\nType the option that best matches your search or type '999' to restart your search.\n\n")                                        
                                except:
                                        uinput = input("Sorry, input needs to be a number!\nType the option that best matches your search or type '999' to restart your search.\n\n")
                                        continue
