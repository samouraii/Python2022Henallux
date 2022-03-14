class Player:

    nb_players = 0 
    def __init__(self, name, pseudo,country):
        self.nom = name
        self.pseudo = pseudo
        self.country = country
        Player.nb_players += 1

    def __str__(self):
        return self.name + " alias " + self.pseudo + " comes from " + self.country.name

    @staticmethod
    def play():
        nb = int(input ("Entrez un nombre entre 1 et 10 : "))
        while not 1<=nb<=10:
            nb = int(input ("Entrez un nombre entre 1 et 10 : "))
        return nb

class Country :

    def __init__ (self, name, capital, players = None):
        self.name = name
        self.capital = capital
        self.players = players or []
    def show_details(self):
        print (self.name, "( Capital : ", self.capital, " ) :")
        for player in self.players :
            print( " - ", player.pseudo )

    def add_player(self, player):
        #retriré de la liste de l'ancien pays
        player.country.players.remove(player)
        self.players.append(player)
        player.country = self


if __name__ == "__main__" :

    usa = Country("USA","Washington")
    bel = Country("Belgique", "Bruxelles")

    print(usa.__dict__)
    print(Player.nb_players)
    print("Création John")
    print("nom du joueru")
    prenom = input()
    john = Player(prenom, "Coucou", usa)
    print(Player.nb_players)
    print("Création Maurice")
    Maurice = Player("Maurice", "MaPoule", bel)
    print(Player.nb_players)

    usa.players.append(john)
    bel.players.append(Maurice)

    bel.show_details()
    usa.show_details()

    print(Player.play())
