#Importing
from Classes.Game import bcolors , Person
from Classes.Spells import Spell
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


#Instantiation Players
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



Player1=Person("THOR",35000,290,670,1000,Player1_Spells,Player1_Items)
Player2=Person("HELA",30000,130,300,900,Player2_Spells,Player2_Items)
Player3=Person("LOKI",27500,250,450,1000,Player3_Spells,Player3_Items)
Players=[Player1,Player2,Player3]

'''
print(Player.Generated_Damage())
print(Player.Generated_Damage())
print(Player.Generated_Damage())
print(Player.Generate_Spell_Dmg(0))
print(Player.Generate_Spell_Dmg(1))
print(Player.Generate_Spell_Dmg(2))
'''

#Instantiation Enemies
Enemy1_Spells=[Thunder,Fire,Cura]
Enemy2_Spells=[Meteor,Quake,Cure,Cura]
Enemy3_Spells=[Fire,Blizzard,Splash,Cure]
Enemy1=Person("SURTUR   ",45000,150,750,1000,Enemy1_Spells,[])
Enemy2=Person("MALEKITH ",23000,275,300,800,Enemy2_Spells,[])
Enemy3=Person("DESTROYER",35000,100,550,1200,Enemy3_Spells,[])
Enemies=[Enemy1,Enemy2,Enemy3]

'''
print(Enemy.Generated_Damage())
print(Enemy.Generated_Damage())
print(Enemy.Generated_Damage())
print(Enemy.Generate_Spell_Dmg(0))
print(Enemy.Generate_Spell_Dmg(1))
print(Enemy.Generate_Spell_Dmg(2))
'''


#Initializing vars and screen
running = True
i=0

print(bcolors.FAIL + bcolors.BOLD +"\tAN ENEMY ATTACKS" + bcolors.ENDC)
print(bcolors.FAIL + "=========================================================================================================================================================================" + bcolors.ENDC)

#Game Starts
while running:

    #HP and MP bars print out
    for Player in Players:
        Player.Get_Stats()
    for Enemy in Enemies:
        Enemy.Get_Enemy_Stats()

    print("\n",bcolors.FAIL+"========================================================================================================================================================================="+ bcolors.ENDC)

    #Player Attacks
    for Player in Players :
        print("\n\t"+bcolors.BOLD+bcolors.HEADER+Player.Name,"'s Chance :"+bcolors.ENDC)
        #Player chooses action
        Player.Choose_Action()
        Choice=input(" \t Choose Action : ")
        Index=int(Choice)-1
        #print("You Chose : ",Choice)

        if(Index==0):
            #Chose simple attack
            Dmg=Player.Generated_Damage()
            Enemy_No=Player.Choose_Target(Enemies)
            Enemies[Enemy_No].Take_Dmg(Dmg)
            print(bcolors.OKGREEN+"\t\t You attacked "+Enemies[Enemy_No].Name.replace(" ","")+" for ",Dmg," Points of health ."+bcolors.ENDC)
            #Checking Enemy Casualities
            if(Enemies[Enemy_No].Get_Hp()==0):
                print(bcolors.BOLD+bcolors.OKGREEN+Enemies[Enemy_No].Name.replace(" ","")+" has dies"+bcolors.ENDC)
                del Enemies[Enemy_No]

        elif(Index==1):
            #Chose to use Magic
            #Choosing Magic
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
                #Chose Nothing
                continue

            Curr_Mp = Player.Get_Mp()

            if(Spell.Cost>Curr_Mp):
                #Not Enough MP for magic
                print(bcolors.FAIL +"\nNOT ENOUGHT MP "+bcolors.ENDC)
                continue

            Player.Reduce_Mp(Spell.Cost)

            if(Spell.Type=="White"):
                #Healing Magic
                Player.Heal(Magic_Dmg)
                print(bcolors.OKBLUE + "\n\t\t",Spell.Name,"Heals for ",str(Magic_Dmg)," HP "+bcolors.ENDC)
            #Player.Reduce_Mp(Spell.Cost)

            elif(Spell.Type=="Black"):
                #Attacking Spells
                Enemy_No = Player.Choose_Target(Enemies)
                Enemies[Enemy_No].Take_Dmg(Magic_Dmg)
                #Enemy.Take_Dmg(Magic_Dmg)
                print(bcolors.OKGREEN + "\n\t\tSPELL : "+Spell.Name+" Deals "+str(Magic_Dmg) + " Points of health to "+Enemies[Enemy_No].Name + bcolors.ENDC)
                #Checking Enemy Casualities
                if (Enemies[Enemy_No].Get_Hp() == 0):
                    print(bcolors.BOLD + bcolors.OKGREEN + Enemies[Enemy_No].Name.replace(" ","") + " has dies" + bcolors.ENDC)
                    del Enemies[Enemy_No]

        elif(Index==2):
            #Chose to use Item
            #Choosing item
            Player.Choose_Item()
            Item_Choice=int(input("\t Choose an Item :"))-1

            if (Item_Choice == -1):
                #Chose nothing
                continue

            Item_Chose=Player.Items[Item_Choice]["Item"]

            if(Player.Items[Item_Choice]["Quantity"]==0):
                #Out of item
                print(bcolors.FAIL,"\n\t\t None Left..." + bcolors.ENDC )
                continue

            Player.Items[Item_Choice]["Quantity"] -=1

            if(Item_Chose.Type=="Potion"):
                #Chose Healing Item
                Player.Heal(Item_Chose.Prop)
                print(bcolors.OKGREEN + "\n\t\t" , Item_Chose.Name + " Heals for " + str(Item_Chose.Prop)," HP",bcolors.ENDC)
                #Item_Chose["Quantity"]-=1

            elif(Item_Chose.Type=="Elixir"):
            #Chose Complete Healers
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
                #Chose Attacking item
                Enemy_No = Player.Choose_Target(Enemies)
                Enemies[Enemy_No].Take_Dmg(Item_Chose.Prop)
                #Enemy.Take_Dmg(Item_Chose.Prop)
                print(bcolors.FAIL+ "\n\t\t", Item_Chose.Name + " Attacks "+Enemies[Enemy_No].Name +" for " + str(Item_Chose.Prop)," HP",bcolors.ENDC)
                #Item_Chose["Quantity"] -= 1
                if (Enemies[Enemy_No].Get_Hp() == 0):
                    print(bcolors.BOLD + bcolors.OKGREEN + Enemies[Enemy_No].Name.replace(" ","") + " has dies" + bcolors.ENDC)
                    del Enemies[Enemy_No]

    #Check if Battle is over
    Defeated_Enemies = 0
    Defeatef_Players = 0
    for Enemy in Enemies:
        if (Enemy.Get_Hp() == 0):
            Defeated_Enemies += 1
    for Player in Players:
        if (Player.Get_Hp() == 0):
            Defeatef_Players += 1

    if (Defeated_Enemies == 3):
        print(bcolors.OKGREEN + "YOU WIN " + bcolors.ENDC)
        running = False
    elif (Defeatef_Players == 3):
        print(bcolors.FAIL + "YOU LOST " + bcolors.ENDC)
        running = False

    print("\n")
    #Enemy attacks
    for Enemy in Enemies:
        #Randomize Action
        Enemy_Choice =  random.randrange(0,2)
        if(Enemy_Choice==0):
            #Chose Normal attack
            #Chose Target
            Target = random.randrange(0, 3)
            Enemy_Dmg = Enemy.Generated_Damage()
            Players[Target].Take_Dmg(Enemy_Dmg)
            print(bcolors.FAIL + "\t\t", Players[Target].Name + " was attacked for ", Enemy_Dmg," Points of health by "+Enemy.Name + bcolors.ENDC)

        elif(Enemy_Choice==1):
            #Chose Magic
            Spell,Magic_Dmg=Enemy.Choose_Enemy_Spell()
            Enemy.Reduce_Mp(Spell.Cost)
            if (Spell.Type == "White"):
                #Chose Healing Magic
                Enemy.Heal(Magic_Dmg)
                print(bcolors.FAIL + "\t\t", Spell.Name, "Heals "+Enemy.Name+"for ", str(Magic_Dmg), " HP " + bcolors.ENDC)
                # Player.Reduce_Mp(Spell.Cost)

            elif (Spell.Type == "Black"):
                #Chose Attacking Magic
                Target = random.randrange(0, 3)
                Players[Target].Take_Dmg(Magic_Dmg)
                # Enemy.Take_Dmg(Magic_Dmg)
                print(bcolors.FAIL +"\t\t"+Enemy.Name+" uses spell : " + Spell.Name + " that Deals " + str(
                    Magic_Dmg) + " Points of health to " + Players[Target].Name + bcolors.ENDC)
                #Checking Casualities
                if (Players[Target].Get_Hp() == 0):
                    print(bcolors.BOLD + bcolors.OKGREEN + Players[Target].Name.replace(" ",
                                                                                          "") + " has died" + bcolors.ENDC)
                    del Players[Target]
            #print ("Enemy chose ",Spell.Name," with damage ",Magic_Dmg)



'''
POSSIBILITIES OF IMPROVEMENT :
1. Using JSON save your game and continue later
2. Introduce a list of enemies and depending upon the experience and level scale the enemy and inreoduce one or more in a level
'''