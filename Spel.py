import random as rand

class Player:
    def __init__(self, inv, strength, lvl, hp):
        self.inv = inv
        self.strength = strength 
        self.lvl = lvl
        self.hp = hp

    def __str__(self):
            ret_str_player = f"Str: {self.strength}, Hp: {self.hp}, Lvl: {self.lvl}"
            return ret_str_player
        
    def look_inv(self):
        ret_inv = self.inv
        return ret_inv
    
äventyrare = Player([], 5, 0, 10)

class Item:
    def __init__ (self, name, strength): #input för namn och styrka för itemet
        self.name = name
        self.strength = strength
   
    def __str__(self): #printar ut namn och styrka
        return(f"namn: {self.name}, str: {self.strength}")

def give_name():
    num = rand.randint(1, 3)
    if num == 1:
        return "Black"
    elif num == 2:
        return "Yellow"
    else:
        return "Blue"

def give_str():
    val = rand.randint(1, 5)
    return val

def chest():
    item = Item(give_name(), give_str())
    äventyrare.inv.append(item)
    print(f"Du fick: {item.name}, str: {item.stength}")
    
#a = int(input("K -> "))

#if a == 1:
#    chest()
#elif a == 3:
#    for i in range(3):
#        chest()
#else:
#    for i in range(2):
#        chest()
        
def calc_str():
    inv_str = 0
    if len(äventyrare.inv) == 1:
        inv_str += äventyrare.inv[0].strength
    elif len(äventyrare.inv) == 2:
        for i in range(0, 2):
            inv_str += äventyrare.inv[i].strength
    elif len(äventyrare.inv) == 3:
        for a in range(0, 3):
            inv_str += äventyrare.inv[a].strength
    elif len(äventyrare.inv) == 4:
        for b in range(0, 4):
            inv_str += äventyrare.inv[b].strength
    else:
        for c in range(0, 5):
            inv_str += äventyrare.inv[c].strength
    tot_str = äventyrare.strength + inv_str
    äventyrare.strength = tot_str
    return int(äventyrare.strength)

#print(calc_str())

#item = Item(Name(), Strength())


def view_inv():
    if len(äventyrare.inv) == 1:
        print(f" 1: {äventyrare.inv[0]}")
    elif len(äventyrare.inv) == 2:
        for i in range(0, 2):
            print(f" {i+1}: {äventyrare.inv[i]}")
    elif len(äventyrare.inv) == 3:
        for a in range(0, 3):
            print(f" {a+1}: {äventyrare.inv[a]}")
    elif len(äventyrare.inv) == 4:
        for b in range(0, 4):
            print(f" {b+1}: {äventyrare.inv[b]}")
    elif len(äventyrare.inv) == 0:
        print("Ditt inventory är tomt")
    else:
        for c in range(0, 5):
            print(f" {i+1}: {äventyrare.inv[c]}")

#print(äventyrare)

def trap():
    d = random.randint(1, 3)
    if d == 1:
        player.hp -= 1
        return print("du gick på en koreansk fälla, du förlorade 1 liv")
    if d == 2:
        player.hp -= 2
        return print("du gick på en japan fälla, du förlorade 1 liv")
    if d == 3:
        player.hp -= 3
        return print("du gick på en vietnamesisk fälla, du förlorade 1 liv")

def combat(self):
    monster = random.randint(1, 20) #ger monstret en random styrka
    if äventyrare.strength > monster:
         player.lvl += 1 #levlar upp äventyraren
         return print("du van över monstret")
     elif äventyrare.strength < monster:
        player.hp -= 1 #minskar äventyrarens hp
        return print("du förlorade över monster")
    else:
        number = random.randint(0, 1) #slumpar vem som vinner om båda har samma styrka
        if number == 1:
            player.lvl += 1 #levlar upp äventyraren
            return print("du van över monstret")
        else:
            player.hp -= 1 #minskar äventyrarens hp
            return print("du förlorade över monster")

def view_stats():
    print(äventyrare)


def room_randomizer():
    print("Vill du gå höger, framåt eller åt vänster?") #ger illusion av kontroll över vilket rum man kommer att få
    while True: #låter spelaren välja vart den ska gå, och om det skrivs fel får de skriva om  
        x = input("--> ")
        x = x.lower()  # konvertera inmatningen till små bokstäver
        if x == "höger" or x == "framåt" or x == "vänster": #breakar loopen om spelaren skrivit korrekt
            break
        else: #låter loopen fortsätta om spelaren skrivit fel
            print("Ogiltigt svar, försök igen")


    y = random.randint(1, 3)
    if y == 1:
        chest()
    if y == 2:
        trap()
    if y == 3:
        combat()
