#Importing
import random

#Colors Definition
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Person Class Definition
class Person:
    #Constructor
    def __init__(self,Name,Hp,Mp,Atk,Df,Magic,Items):
        self.MaxHp=Hp
        self.Hp=Hp
        self.MaxMp=Mp
        self.Mp=Mp
        self.Df=Df
        self.Atkl=Atk-10
        self.Atkh=Atk+10
        self.Magic=Magic
        self.Items=Items
        self.Actions=[" Attack "," Magic "," Items"]
        self.Name=Name

    #Person Methods
    def Generated_Damage(self):
        return random.randrange(self.Atkl,self.Atkh)

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

    def Heal(self,Dmg):
        self.Hp +=Dmg
        if(self.Hp>self.MaxHp):
            self.Hp=self.MaxHp


    def Choose_Action(self):
        i=1
        print((bcolors.OKBLUE + bcolors.BOLD +"\tACTIONS" + bcolors.ENDC))
        for Item in self.Actions:
            print("\t",str(i) + "." , Item)
            i+=1

    def Choose_Magic(self):
        i=1
        print("\n",bcolors.OKBLUE + bcolors.BOLD +"\tMAGIC" + bcolors.ENDC)
        for Spell in self.Magic:
            print("\t",str(i) + "." ,Spell.Name, " (Cost : " , str(Spell.Cost) + ")")
            i+=1

    def Choose_Item(self):
        i=1
        print("\n",bcolors.OKGREEN + bcolors.BOLD+"\tITEMS"+ bcolors.ENDC)
        for Item in self.Items :
            print("\t",str(i),".",Item["Item"].Name," : ",Item["Item"].Desc,"( x", str(Item["Quantity"]),")")
            i=i+1

    def Choose_Target(self, Enemies):
        i = 1
        print("\n", bcolors.FAIL + bcolors.BOLD + "\tTARGET" + bcolors.ENDC)
        for Enemy in Enemies:
            if(Enemy.Get_Hp()!=0):
                print("        "+str(i)+". "+Enemy.Name)
                i = i + 1
        Choice=int(input("\t Choose Target : "))-1
        return Choice

    def Choose_Enemy_Spell(self):
        Magic_Choice = random.randrange(0, len(self.Magic))
        Spell = self.Magic[Magic_Choice]
        Magic_Dmg = Spell.Generated_Spell_Dmg()

        Pct=(self.Hp/self.MaxHp) *100
        if(self.Mp<Spell.Cost or Spell.Type=="White" and Pct<50):
            self.Choose_Enemy_Spell()
        else:
            return Spell,Magic_Dmg

    def Get_Enemy_Stats(self):
        Hp_Bar = ""
        Mp_Bar = ""
        Hp_ticks = (self.Hp / self.MaxHp) * 25
        Mp_ticks = (self.Mp / self.MaxMp) * 10

        while Hp_ticks > 0:
            Hp_Bar += "█"
            Hp_ticks -= 1
        while Mp_ticks > 0:
            Mp_Bar += "█"
            Mp_ticks -= 1
        while len(Hp_Bar) < 25:
            Hp_Bar += " "
        while len(Mp_Bar) < 10:
            Mp_Bar += " "

        Hp_String = str(self.Hp) + "/" + str(self.MaxHp)
        Curr_Hp_string = ""

        if (len(Hp_String) < 11):
            Dec = 11 - len(Hp_String)
            while Dec > 0:
                Curr_Hp_string += " "
                Dec -= 1
            Curr_Hp_string += Hp_String
        else:
            Curr_Hp_string += Hp_String

        Mp_String = str(self.Mp) + "/" + str(self.MaxMp)
        Curr_Mp_string = ""

        if (len(Mp_String) < 7):
            Dec = 7 - len(Mp_String)
            while Dec > 0:
                Curr_Mp_string += " "
                Dec -= 1
            Curr_Mp_string += Mp_String
        else:
            Curr_Mp_string += Mp_String

        print("                                     _________________________                __________")
        print(bcolors.BOLD +bcolors.HEADER + self.Name+" :"+bcolors.ENDC,"          " + Curr_Hp_string + "   |" + bcolors.FAIL + Hp_Bar + bcolors.ENDC + bcolors.BOLD + "| \t" + Curr_Mp_string + "  |" + bcolors.OKBLUE + Mp_Bar + bcolors.ENDC + "|")


    def Get_Stats(self):
            Hp_Bar=""
            Mp_Bar=""
            Hp_ticks=(self.Hp/self.MaxHp)*25
            Mp_ticks=(self.Mp/self.MaxMp)*10

            while Hp_ticks>0:
                Hp_Bar+="█"
                Hp_ticks-=1
            while Mp_ticks>0:
                Mp_Bar+="█"
                Mp_ticks-=1
            while len(Hp_Bar)<25:
                Hp_Bar+=" "
            while len(Mp_Bar)<10:
                Mp_Bar+=" "

            Hp_String = str(self.Hp) + "/" + str(self.MaxHp)
            Curr_Hp_string = ""

            if (len(Hp_String) < 11):
                Dec = 11 - len(Hp_String)
                while Dec > 0:
                    Curr_Hp_string += " "
                    Dec -= 1
                Curr_Hp_string += Hp_String
            else:
                Curr_Hp_string += Hp_String

            Mp_String = str(self.Mp) + "/" + str(self.MaxMp)
            Curr_Mp_string = ""

            if (len(Mp_String)<7):
                Dec = 7 - len(Mp_String)
                while Dec > 0:
                    Curr_Mp_string += " "
                    Dec -= 1
                Curr_Mp_string += Mp_String
            else:
                Curr_Mp_string += Mp_String

            print("                                     _________________________                __________")
            print(bcolors.BOLD+bcolors.HEADER + self.Name+"      :"+bcolors.ENDC,"          "+Curr_Hp_string+"   |" + bcolors.OKGREEN + Hp_Bar + bcolors.ENDC + bcolors.BOLD + "| \t"+Curr_Mp_string+"  |" + bcolors.OKBLUE + Mp_Bar + bcolors.ENDC + "|")





