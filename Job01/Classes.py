class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def afficher(self):
        print(f"Longueur : {self.__longueur}, Largeur : {self.__largeur}")


# Création d'un rectangle avec une longueur de 10 et une largeur de 5
mon_rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
mon_rectangle.afficher()

# Modification de la longueur et de la largeur
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(7)

# Affichage des valeurs après modification
mon_rectangle.afficher()
