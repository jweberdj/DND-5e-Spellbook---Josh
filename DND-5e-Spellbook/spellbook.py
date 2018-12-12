import requests
import json
import textwrap
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from prettytable import PrettyTable

class Spellbook(object):
        def __init__(self):
                self.spells = requests.get('http://dnd5eapi.co/api/spells').json()['results']

        def printSpell(self, spelldata):
                
                t = PrettyTable()
                t.field_names = ['Spell Attribute','Description']
                components = ''
                for p in spelldata['components']:
                        components += ' {}'.format(p)

                print('{}\n'.format(spelldata['name']).title())
                try:
                        t.add_row(['Higher Level', spelldata['higher_level'][0]])
                except KeyError:
                        t.add_row(['Higher Level', '--'])
                t.add_row(['Page', spelldata['page']])
                t.add_row(['Range', spelldata['range']])
                t.add_row(['Components', components])
                try:   
                        t.add_row(['Material', spelldata['material']])
                except:
                        t.add_row(['Material', '--'])
                t.add_row(['Ritual', spelldata['ritual']])
                t.add_row(['Duration', spelldata['duration']])
                t.add_row(['Concentration', spelldata['concentration']])
                t.add_row(['Casting Time', spelldata['casting_time']])
                if spelldata['level'] == -1:
                        t.add_row(['Casting Level', 'Cantrip'])
                else:
                        t.add_row(['Casting Level', spelldata['level']])
                t.add_row(['Magic School', spelldata['school']['name']])
                t.add_row(['Description', textwrap.fill(spelldata['desc'][0], width=50)])
                print(t)

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
                        inputerror = True
                        qresults = self.spellSearch(spell)
                        for num,r in enumerate(qresults, start=1):
                                print("{}. {}\n".format(num, r))
                        
                        while inputerror:
                                uinput = input("Type the option that best matches your search or type '-r' to restart your search.\n\n")
                                if int(uinput) in range(len(qresults)+1):
                                        self.readSpell(qresults[str(uinput-1)])
                                        inputerror = False
                                elif uinput == '-r':
                                        inputerror = False
                                        pass
                                else:
                                        print("Sorry, that's not an option!")
