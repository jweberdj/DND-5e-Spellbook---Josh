import requests
import json

class Spellbook:
        def __init__(self,name='My Spellbook',spells=[]):
                self.name = name
                self.spells = spells

        def getSpellData(self, spellURL):
                # input: str
                return requests.get(spellURL).json()

        def printSpell(self, spelldata):
                components = ''
                for p in spelldata['components']:
                        components += ' {}'.format(p)
                print('\n----------------------\n- Spell Name: {}\n-----------------\n'.format(spelldata['name']))
                print('- Description: {}\n'.format(spelldata['desc'][0]))
                print('- At a Higher Level: {}\n'.format(spelldata['higher_level'][0]))
                print('- Page: {}\n'.format(spelldata['page']))
                print('- Range: {}\n'.format(spelldata['range']))
                print('- Components: {}\n'.format(components))
                #print('- Material: {}\n'.format(spelldata['material']))
                print('- Ritual: {}\n'.format(spelldata['ritual']))
                print('- Duration: {}\n'.format(spelldata['duration']))
                print('- Concentration: {}\n'.format(spelldata['concentration']))
                print('- Casting Time: {}\n'.format(spelldata['casting_time']))
                print('- Casting Level: {}\n'.format(spelldata['level']))
                print('- Magic School: {}\n'.format(spelldata['school']['name']))

        def readSpell(self, spell):
                # input: str
                found = False
                if isinstance(spell, str):
                        for x in self.spells:
                                if x['name'].lower() == spell.lower():
                                        spellData = self.getSpellData(x['url'])
                                        self.printSpell(spellData)
                                        found = True
                                        break
                                else:
                                        pass
                        if not found:
                                print('\nThe spell {} was not found.'.format(spell))   
                else:
                        error=('ERROR: the parameter - "{}" -  passed to "readSpell" is not a "string".'.format(spell))
                        raise Exception(error)
                
