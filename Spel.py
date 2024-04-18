import random


class Player():
    def __init__(self, inv, strength, lvl, hp):
        self.inv = inv
        self.strength = strength
        self.lvl = lvl
        self.hp = hp


    def __str__(self):
            ret_str_player = f"Str: {self.strength}, Hp: {self.hp}, Lvl: {self.lvl}"
            return ret_str_player
       
class Item:
    def __init__ (self, name, strength): #input för namn och styrka för itemet
        self.name = name
        self.strength = strength
   
    def __str__(self): #printar ut namn och styrka
        return(f"namn: {self.name} \nstyrka: {self.strength}")


player = Player([], 5, 0, 25)


def give_name():
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


    y = random.randint(1, 3)
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
    d = random.randint(1, 3)
    if d == 1:
        player.hp -= 1
        return print(f"\nDu gick på en koreansk fälla, du förlorade 1 liv")
    if d == 2:
        player.hp -= 2
        return print(f"\nDu gick på en japan fälla, du förlorade 2 liv")
    if d == 3:
        player.hp -= 3
        return print(f"\nDu gick på en vietnamesisk fälla, du förlorade 3 liv")


def Strength():
    val = random.randint(1, 5)
    return val


def calc_str():
    inv_str = 0
    player.strength = 5
    for i in player.inv:
       inv_str += i.strength
    tot_str = player.strength + inv_str
    player.strength = tot_str


def chest():
    holder = Item(give_name(), Strength())
    player.inv.append(holder)
    print(holder)
    calc_str()


def view_inv():
    for i in player.inv:
        print(i)


g = 0


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


def play():
    while True:
        print(f"\nVad vill du göra nu\n1. Kolla ditt inventory\n2. Kolla dina stats\n3. Gå in ett nytt rum\nSvara 1, 2 eller 3")
        while True:
            e = input("--> ")
            if e == "1":
                view_inv()
                break
            if e == "2":
                print(player)
                break
            if e == "3":
                room_randomizer()
                break
            else:
                print("felaktig inmatning, försök igen")
        if player.lvl == 10:
            print(f"n\Du har klarat spelet!")
            break
        if player.hp <= 0:
            print(f"\nDu dog")
            break


while True:
    print("Välkommen till Michael Jacksons dungeon")
    play()
    print(f"\nVill du spela igen? Ja eller Nej")
    while True:
        f = input("--> ")
        if f.lower() == "ja":
            print("Då kör vi!")
            player = Player([], 5, 0, 25)
            break
        elif f.lower() == "nej":
            print("Hej då")
            g = 1
            break
        else:
            print("Felaktig input, försök igen")
    if g == 1:
        break
