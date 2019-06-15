import random

class Attacker:
    '''to make the class more dynamic'''

    def __init__(self,atk1,atk2):
        self.atkl=atk1
        self.atkh=atk2

    def GetDamage(self):
        return random.randrange(self.atkl,self.atkh,5)

Attk1=Attacker(20,60)
print(Attk1.GetDamage())

Attk2=Attacker(35,73)
print(Attk2.GetDamage())
