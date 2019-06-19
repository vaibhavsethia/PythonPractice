#Importing
from Classes.Game import bcolors , Person
from Classes.Magic import Spell
from Classes.Inventory import Item
import random

#Creating Black Magic
Fire=Spell("Fire",50,7500,"Black")
Blizzard=Spell("Blizzard",20,2500,"Black")
Quake=Spell("Quake",2,500,"Black")
Thunder=Spell("Thunder",35,4000,"Black")
Meteor=Spell("Meteor",60,8000,"Black")
Splash=Spell("Splash",7,1100,"Black")


#Creating White Magic
Cure=Spell("Cure",25,4500,"White")
Cura=Spell("Cura",40,7700,"White")


#Create some Items
Potion=Item("Potion","Potion","Heals",3000)
HighPotion=Item("Hi-Potion","Potion","Heals 100",6000)
SuperPotion=Item("Su-Potion","Potion","Heals 500 ",10000)
Elixir=Item("Elixir","Elixir","Fully Restores one party Member",99999)
MegaElixir=Item("Mega-Elixir","Elixir","Fully Restores all party Member",99999)
Grenade=Item("Grenade","Attack","Deals 500 Damage",5700)
Molotov=Item("Molotov","Attack","Deals 250 Damage",3250)
Spikes=Item("Spikes","Attack","Deals 200 Damage",2200)
NinjaStars=Item("Ninja-Stars","Attack","Deals 400 Damage",4600)


#Instantiation Persons
Player1_Spells=[Fire,Thunder,Meteor,Splash,Cure,Cura]
Player1_Items=[{"Item":Potion,"Quantity":10},{"Item":HighPotion,"Quantity":2},
                {"Item":Elixir,"Quantity":3},{"Item":MegaElixir,"Quantity":1},
                {"Item":Molotov,"Quantity":5},{"Item":NinjaStars,"Quantity":5}]
Player2_Spells=[Fire,Thunder,Meteor,Splash,Cure,Cura]
Player2_Items=[{"Item":Potion,"Quantity":10},{"Item":HighPotion,"Quantity":2},
                 {"Item":Elixir,"Quantity":3},{"Item":MegaElixir,"Quantity":1},
                {"Item":Molotov,"Quantity":5},{"Item":NinjaStars,"Quantity":5}]
Player3_Spells=[Fire,Thunder,Meteor,Splash,Cure,Cura]
Player3_Items=[{"Item":Potion,"Quantity":10},{"Item":HighPotion,"Quantity":2},
                {"Item":Elixir,"Quantity":3},{"Item":MegaElixir,"Quantity":1},
                {"Item":Molotov,"Quantity":5},{"Item":NinjaStars,"Quantity":5}]



Player1=Person("THOR",29500,290,670,1000,Player1_Spells,Player1_Items)
Player2=Person("HELA",24000,130,300,900,Player2_Spells,Player2_Items)
Player3=Person("LOKI",23500,250,450,1000,Player3_Spells,Player3_Items)
Players=[Player1,Player2,Player3]
#Player3.Get_Stats()

'''
print(Player.Generated_Damage())
print(Player.Generated_Damage())
print(Player.Generated_Damage())
print(Player.Generate_Spell_Dmg(0))
print(Player.Generate_Spell_Dmg(1))
print(Player.Generate_Spell_Dmg(2))
'''

Enemy=Person("SURTUR",125000,1000,750,2500,[],[])
'''
print(Enemy.Generated_Damage())
print(Enemy.Generated_Damage())
print(Enemy.Generated_Damage())
print(Enemy.Generate_Spell_Dmg(0))
print(Enemy.Generate_Spell_Dmg(1))
print(Enemy.Generate_Spell_Dmg(2))
'''
#Game Starts
running = True
i=0

print(bcolors.FAIL + bcolors.BOLD +"\tAN ENEMY ATTACKS" + bcolors.ENDC)
print(bcolors.FAIL + "=========================================================================================================================================================================" + bcolors.ENDC)
while running:
    '''
    print("Lets Overflow ")
    i++
    '''
    for Player in Players:
        Player.Get_Stats()
    Enemy.Get_Enemy_Stats()
    print("\n",bcolors.FAIL+"========================================================================================================================================================================="+ bcolors.ENDC)

    for Player in Players :
        print("\n\t"+bcolors.BOLD+bcolors.HEADER+Player.Name,"'s Chance :"+bcolors.ENDC)
        Player.Choose_Action()
        Choice=input(" \t Choose Action : ")
        Index=int(Choice)-1
        #print("You Chose : ",Choice)

        if(Index==0):
            Dmg=Player.Generated_Damage()
            Enemy.Take_Dmg(Dmg)
            print(bcolors.OKGREEN+"\t\t You attacked for ",Dmg," Points of health ."+bcolors.ENDC)

        elif(Index==1):
            Player.Choose_Magic()
            Magic_Choice=int(input("\t Choose magic: "))-1
            Spell=Player.Magic[Magic_Choice]
            Magic_Dmg=Spell.Generated_Spell_Dmg()

            '''
            Magic_Dmg=Player.Generate_Spell_Dmg(Magic_Choice)
            Spell=Player.Get_SpellName(Magic_Choice)
            Spell_Cost=Player.Get_SpellMpCost(Magic_Choice)
            '''
            if(Magic_Choice==-1):
                continue

            Curr_Mp = Player.Get_Mp()

            if(Spell.Cost>Curr_Mp):
                print(bcolors.FAIL +"\nNOT ENOUGHT MP "+bcolors.ENDC)
                continue

            Player.Reduce_Mp(Spell.Cost)

            if(Spell.Type=="White"):
                Player.Heal(Magic_Dmg)
                print(bcolors.OKBLUE + "\n\t\t",Spell.Name,"Heals for ",str(Magic_Dmg)," HP "+bcolors.ENDC)
            #Player.Reduce_Mp(Spell.Cost)

            elif(Spell.Type=="Black"):
                Enemy.Take_Dmg(Magic_Dmg)
                print(bcolors.OKGREEN + "\n\t\tSPELL : "+Spell.Name+" Deals "+str(Magic_Dmg) + " Points of health " + bcolors.ENDC)

        elif(Index==2):
            Player.Choose_Item()
            Item_Choice=int(input("\t Choose an Item :"))-1

            if (Item_Choice == -1):
                continue

            Item_Chose=Player.Items[Item_Choice]["Item"]

            if(Player.Items[Item_Choice]["Quantity"]==0):
                print(bcolors.FAIL,"\n\t\t None Left..." + bcolors.ENDC )
                continue

            Player.Items[Item_Choice]["Quantity"] -=1

            if(Item_Chose.Type=="Potion"):
                Player.Heal(Item_Chose.Prop)
                print(bcolors.OKGREEN + "\n\t\t" , Item_Chose.Name + " Heals for " + str(Item_Chose.Prop)," HP",bcolors.ENDC)
                #Item_Chose["Quantity"]-=1

            elif(Item_Chose.Type=="Elixir"):

                if(Item_Chose.Name=="Mega-Elixir"):
                    for i in Players :
                        i.Hp = i.MaxHp
                        i.Mp = i.MaxMp
                else:
                    Player.Hp=Player.MaxHp
                    Player.Mp=Player.MaxMp
                print(bcolors.OKGREEN + "\n\t\t",Item_Chose.Name," Fully Restores MP/HP"+bcolors.ENDC)
                #Item_Chose["Quantity"] -= 1

            elif(Item_Chose.Type=="Attack"):
                Enemy.Take_Dmg(Item_Chose.Prop)
                print(bcolors.FAIL+ "\n\t\t", Item_Chose.Name + " Attacks for " + str(Item_Chose.Prop)," HP",bcolors.ENDC)
                #Item_Chose["Quantity"] -= 1

        Enemy_Choice = 1
        Target=random.randrange(0,3)
        Enemy_Dmg = Enemy.Generated_Damage()

        Players[Target].Take_Dmg(Enemy_Dmg)
        print(bcolors.FAIL+"\t\t",Players[Target].Name+" was attacked for ", Enemy_Dmg, " Points of health ."+bcolors.ENDC)


    if(Enemy.Get_Hp()==0):
        print(bcolors.OKGREEN + "YOU WIN " +bcolors.ENDC)
        running=False
    elif(Player.Get_Hp() == 0):
        print(bcolors.FAIL + "YOU LOST " + bcolors.ENDC)
        running = False


