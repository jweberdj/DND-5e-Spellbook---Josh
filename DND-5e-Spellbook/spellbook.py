import requests
import json

class Spellbook:
        def __init__(self,name='My Spellbook',spells=[]):
                self.name = name
                self.spells = spells

        def findSpell(self, spellname):
                ####################################
                ## spellbook = list of dictionaries
                ## spellname = string
                ##########
                ## NEXT CHANGE:
                ## Call to API and get information about the spell
                ## Return the API JSON response
                ####################################
                for spell in self.spells:
                        if spell['name'].lower() == spellname.lower():
                                return spell
                                break
                        else:
                                pass

        def readSpell(self, spell):
                if isinstance(spell, str):
                        for x in self.spells:
                                if x['name'].lower() == spell.lower():
                                        print("Spell Name: {}\nSpell URL: {}".format(x['name'],x['url']))
                                else:
                                        pass
                elif isinstance(spell, dict):
                        for x in self.spells:
                                if x == spell:
                                        print("Spell Name: {}\nSpell URL: {}".format(x['name'],x['url']))
                                else:
                                        pass
                else:
                        print('ERROR: the parameter passed to "readSpell" is not a "string" or "list".')