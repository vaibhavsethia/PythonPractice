#Importing
import random

#Spell Definition
class Spell:
    #Constructor
    def __init__(self,Name,Cost,Dmg,Type):
        self.Name=Name
        self.Cost=Cost
        self.Dmg=Dmg
        self.Type=Type

    #Spell methods
    def Generated_Spell_Dmg(self):
        return random.randrange(self.Dmg-15,self.Dmg+15)
