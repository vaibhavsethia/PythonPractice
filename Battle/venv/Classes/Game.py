import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    def __init__(self,Hp,Mp,Atk,Df,Magic):
        self.MaxHp=Hp
        self.Hp=Hp
        self.MaxMp=Mp
        self.Mp=Mp
        self.Atkl=Atk-10
        self.Atkh=Atk+10
        self.Magic=Magic
        self.Actions=[" Attack "," Magic "]

    def Generated_Damage(self):
        return random.randrange(self.Atkl,self.Atkh)

    def Generate_Spell_Dmg(self,i):
        Mgl=self.Magic[i]["Dmg"] -5
        Mgh=self.Magic[i]["Dmg"] +5
        return random.randrange(Mgl,Mgh)

    def Take_Dmg(self,Dmg):
        self.Hp -=Dmg
        if(self.Hp<0):
            self.Hp=0
        return self.Hp

    def Get_Hp(self):
        return self.Hp

    def Get_MaxHp(self):
        return self.MaxHp

    def Get_Mp(self):
        return self.Mp

    def Get_MaxMp(self):
        return self.MaxMp

    def Reduce_Mp(self,Cost):
        self.Mp -=Cost

    def Get_SpellName(self,i):
        return self.Magic[i]["Name"]

    def Get_SpellMpCost(self,i):
        return self.Magic[i]["Cost"]

    def Choose_Action(self):
        i=1
        print("ACTIONS")
        for Item in self.Actions:
            print(str(i) + ":" ,Item)

    def Choose_Magic(self):
        i=1
        print(("MAGIC"))
        for Spell in self.Magic:
            print(str(i) + ":" ,Spell["Name"], " Cost : " , str(Spell["Mp"]) + ")")



