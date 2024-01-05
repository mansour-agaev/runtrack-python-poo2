class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

    def afficher(self):
        print(f"Titre : {self.__titre}, Auteur : {
              self.__auteur}, Nombre de pages : {self.__nb_pages}")


# Création d'un livre
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)

# Affichage des valeurs initiales
mon_livre.afficher()

# Modification du titre, de l'auteur et du nombre de pages
mon_livre.set_titre("Harry Potter")
mon_livre.set_auteur("J.K. Rowling")
# Modification du nombre de pages avec une valeur valide
mon_livre.set_nb_pages(300)
mon_livre.afficher()

# Tentative de modifier le nombre de pages avec une valeur non valide
# Ceci affichera un message d'erreur car le nombre de pages est invalide
mon_livre.set_nb_pages(-50)
