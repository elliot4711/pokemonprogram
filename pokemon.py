class Pokemon:

    def __init__(self, name, type1, type2, total, HP, attack, defense,specatk, specdef, speed, generation, legendary):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.specatk = specatk
        self.specdef = specdef
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return(str((self.name, self.type1, self.type2, self.total, self.HP, self.attack, self.defense,self.specatk, self.specdef, self.speed, self.generation, self.legendary)))
    
    def name1(self):
        return(self.name)
    
    def __lt__(self, other): 
        return self.HP < other.HP     
    
    def attack1(self, other):
        if self.attack < other.attack:
            return "opponent wins"
        else:
            return "you win"
    
    def defense1(self, other):
        if self.defense < other.defense:
            return "opponent wins"
        else:
            return "you win"
"""
bulbasaur = Pokemon("Bulbasaur","Grass","Poison",318,45,49,49,65,65,45,1,False)
ivysaur = Pokemon("Ivysaur","Grass","Poison",405,60,62,63,80,80,60,1,False)
print(bulbasaur)
print(ivysaur)
print(bulbasaur < ivysaur)
print(bulbasaur.attack1(ivysaur))
print(bulbasaur.defense1(ivysaur))
"""

def createpokemon():
    f = open("pokemon.csv", "r")
    pokemonlist = list()
    for line in f:
        line.strip("\n")
        line = line.split(",")
        pokemonlist.append(Pokemon(line[1], line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]))
    
    return pokemonlist

pokemonlist = createpokemon()

name = input("What pokemon are you searching for?")

def search(name, pokemonlist):
    for pokemon in pokemonlist:
        if pokemon.name1() == name:
            print(pokemon)
            break

search(name, pokemonlist)