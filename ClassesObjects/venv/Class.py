import random
class Enemy:
    Hp=200
    Mp=100

    def __init__(self,var1,var2):
        self.atkl=var1
        self.atkh=var2

    def GetHp(self):
        return self.Hp

    def GetMp(self):
        return self.Mp

    def GetAtk(self):
        return random.randrange(self.atkl,self.atkh)
