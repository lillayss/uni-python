# lezioni sulle classi prof rodola'

# player_name = "Gianni"
# player_height = 1.78
# player_atp_points  = 5000
# player_is_left_handed = False
# player_ranking = 7
# player_nationality = "Italian"
# player_has_won = True


class player:

    def __init__(self, name: str, height: float, atp: int): # constructor
        self.name = name
        self.height = height
        self.atp = atp
        self.squared_atp = atp**2

    def __str__(self) -> str:
        return f"name: {self.name}, height: {self.height}, atp: {self.atp}"

    def calc_strenght_(self, alpha: int): #in-place 
        self.strenght = self.squared_atp + self.height * alpha    


# Ereditarieta'

class player_double(player):
    def __init__(self):
        self.position = "Left"
# La classe player_double eredità tutte gli attributi di player


# instance of 'player' class == object of 'player' type
# per convenzione si mette un _ al fine della funzione per dire che sono in-place

gianni = player(name = "Gianni", 
                height = 1.78, 
                atp = 5000) 

gianni.calc_strenght_(alpha = 20)
print(gianni.strenght)

# La classe e' un concetto astratto ! ! !
# Quando la si definisce poi diventa concreto (esempio con gli int)

print(type(gianni))
print(gianni.name)
print(gianni)

# Gianni a.k.a. andrea fa un casino questo uguale

andrea = gianni
andrea.name = "andrea"
print(andrea.name)
print(gianni.name)

# deep copy, occorre mettere un metodo speciale dentro la classe
