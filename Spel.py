import random
import time




class Player():
    def __init__(self, inv, strength, lvl, hp): #skapar attributerna
        self.inv = inv
        self.strength = strength
        self.lvl = lvl
        self.hp = hp




    def __str__(self): #printar stats
            ret_str_player = f"\nStr: {self.strength}, Hp: {self.hp}, Lvl: {self.lvl}"
            return ret_str_player
       
class Item:
    def __init__ (self, name, strength): #input för namn och styrka för itemet
        self.name = name
        self.strength = strength
   
    def __str__(self): #printar ut namn och styrka
        return(f"{player.inv.index(self) + 1}: {self.name} \nstyrka: {self.strength}")




player = Player([], 5, 0, 20) #Ger player stats




def give_name(): #ger random namn från en lista
    b = random.randint(0, len(item_names)-1)
    c = item_names[b]
    item_names.pop(b)
    return c




def room_randomizer():
    print(f"\nVill du gå höger, framåt eller åt vänster?") #ger illusion av kontroll över vilket rum man kommer att få
    while True: #låter spelaren välja vart den ska gå, och om det skrivs fel får de skriva om  
        x = input("--> ")
        x = x.lower()  # konvertera inmatningen till små bokstäver
        if x == "höger" or x == "framåt" or x == "vänster": #breakar loopen om spelaren skrivit korrekt
            break
        else: #låter loopen fortsätta om spelaren skrivit fel
            print("Ogiltigt svar, försök igen")




    y = random.randint(1, 3) #ger random nummer för att ge random rum
    if y == 1:
        print(f"\nDu hittade en kista")
        chest()
    if y == 2:
        trap()
    if y == 3:
        combat()




def combat():
        monster = random.randint(1, 25) #ger monstret en random styrka
        print(f"Monstret har {monster} styrka")
        if player.strength > monster:
            player.lvl += 1 #levlar upp äventyraren
            return print(f"Du vann över monstret")
        elif player.strength < monster:
            player.hp -= 1 #minskar äventyrarens hp
            return print(f"Du förlorade över monster")
        else:
            number = random.randint(0, 1) #slumpar vem som vinner om båda har samma styrka
            if number == 1:
                player.lvl += 1 #levlar upp äventyraren
                return print(f"Du van över monstret")
            else:
                player.hp -= 1 #minskar äventyrarens hp
                return print(f"Du förlorade över monster")




def trap():
    l = random.randint(0, len(think_fast)-1) #random nummer med längden av think_fast listan
    start_time = time.time() #kollar tiden i början av funktionen
    print(f"\nSkriv: ", end="")
    print(think_fast[l]) #printer ett random ord från think_fast med l variabeln
    while True:
        m = input("--> ")
        if time.time() - start_time >= 4: #jämför nuvarande tiden med tiden i början av funktionen
            d = random.randint(1, 3)
            if d == 1:
                player.hp -= 1
                print(f"\nDu var för långsam och förlorade 1 liv")
                break
            if d == 2:
                player.hp -= 2
                print(f"\nDu var för långsam och förlorade 2 liv")
                break
            if d == 3:
                player.hp -= 3
                print(f"\nDu var för långsam och förlorade 3 liv")
                break
        elif m == think_fast[l]: #Kollar om man skrivit rätt
            print(f"\nDu undvek fällan")
            break
        else: print("Du skrev fel, försök igen")




           




def Strength(): #ger random strength till items
    val = random.randint(1, 5)
    return val




def calc_str(): #kalkylerar strength
    inv_str = 0
    player.strength = 5
    for i in player.inv:
       inv_str += i.strength
    tot_str = player.strength + inv_str
    player.strength = tot_str




def chest(): #Skapar ett item och lägger till i player inventory
    holder = Item(give_name(), Strength())
    player.inv.append(holder)
    print(holder)
    if len(player.inv) >= 6: #Om inventoryt är fullt kommer man bli tvungen att ta bort ett item
        print(f"Ditt inventory är fullt, du måste välja släppa ett item")
        view_inv()
        print(f"\nVilket item vill du släppa, skriv mellan 1-6")
        while True:
            h = input("--> ") #beroende på input tar den bort korresponderande item
            if h == "1": 
                del(player.inv[0]) 
                break
            if h == "2":
                del(player.inv[1])
                break
            if h == "3":
                del(player.inv[2])
                break
            if h == "4":
                del(player.inv[3])
                break
            if h == "5":
                del(player.inv[4])
                break
            if h == "6":
                del(player.inv[5])
                break  
            print("Felaktig inmatning försök igen")
    calc_str()




def view_inv(): #printar spelarens inventory
    if not player.inv:
        print("Ditt inventory är tomt.")
    else:
        for i in player.inv:
            print(i)






g = 0 #tillåter oss avsluta en spelet när värdet ändras till 1


#Lista på namn till items
item_names  = ["Shadowstrike Dagger",
"Thunderstorm Maul",
"Frostbite Lance",
"Venomspine Whip",
"Phoenix Fury Bow",
"Runeblade of the Ancients",
"Stormcaller Scepter",
"Celestial Staff of Harmony",
"Dragonfire Bracer",
"Soulreaper Scythe",
"Deaths Embrace Axe",
"Ironclad Tower Shield",
"Serpent Scale Cloak",
"Arcane Orb of Destruction",
"Golems Fist Gauntlet",
"Blazefury Longsword",
"Frostwind Dagger",
"Leviathans Bite Trident",
"Wyverns Winged Blade",
"Voidforged Bastion",
"Bloodthirster Battleaxe",
"Thunderclap Warhammer",
"Hellfire Scimitar",
"Stormsurge Trident",
"Doombringer Sword",
"Shadowmeld Knife",
"Frostbite Javelin",
"Venomous Crossbow",
"Phoenix Feather Wand",
"Celestial Hammer of Light",
"Shadowcloak Hood",
"Thunderforge Helmet",
"Frostweave Robes",
"Venomhide Chestplate",
"Phoenix Feather Cloak",
"Stormguard Helm",
"Celestial Plate Armor",
"Dragonbone Greaves",
"Runebound Gauntlets",
"Soulwarden Circlet",
"Deathbane Hood",
"Ironclad Shieldbearers Armor",
"Serpent Scale Leggings",
"Arcane Robes of Protection",
"Golemheart Helm",
"Blazeguard Pauldrons",
"Frostguard Breastplate",
"Leviathan Scale Mail",
"Wyvernwing Helm",
"Voidforged Vanguard Armor",
"Chads Thundercock"]


#Ord till trap
think_fast = ["for democracy", 
"automatons",
"terminds",
"for superearth",
"friendly fire",
"malevolent creek",
"->->^",
"communist scum"]




def play(): #ger en input så spelaren kan välja vad den vill göra
    while True:
        print(f"\nVad vill du göra nu\n1. Kolla ditt inventory\n2. Kolla dina stats\n3. Gå in ett nytt rum\nSvara 1, 2 eller 3")
        while True: #tillåter oss att göra den inmatningssäker
            e = input("--> ")
            if e == "1":
                view_inv() #kollar spelarens inventory
                break
            if e == "2":
                print(player) #kollar spelarens statistiker
                break
            if e == "3":
                room_randomizer() #går in i ett nytt rum
                break
            else:
                print("felaktig inmatning, försök igen")
        if player.lvl == 10: #avslutar play loop och därmed funktionen
            print(f"\nDu har klarat spelet!")
            break
        if player.hp <= 0:
            print(f"\nDu dog") #avslutar play loop och därmed funktionen
            break




while True: #själva spelet startas och loopar om man vill spela flera gånger
    print("Välkommen till The Dark Dungeon")
    play()
    print(f"\nVill du spela igen? Ja eller Nej") #tillåter att spela igen
    while True: #inmatnings säkerhet
        f = input("--> ")
        if f.lower() == "ja":
            print("Då kör vi!")
            player = Player([], 5, 0, 20) #resettar player stats
            break #inmatnings loopen
        elif f.lower() == "nej": #sätter g som 1 för att breaka loopen som spelar spelet
            print("Hej då")
            g = 1
            break
        else:
            print("Felaktig input, försök igen")
    if g == 1:
        break #avbryter loopen hela koden
