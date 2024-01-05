class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True  # attribut privé initialisé par défaut à True

    def verification(self):
        # Vérifie si le livre est disponible
        return self.disponible

    def emprunter(self):
        # Rend le livre indisponible s'il est disponible
        if self.verification():  # Vérifie si le livre est disponible
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{
                  self.titre}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        # Rend le livre disponible s'il a été emprunté
        if not self.verification():  # Vérifie si le livre a été emprunté (non disponible)
            self.disponible = True
            print(f"Le livre '{self.titre}' a été rendu.")
        else:
            print(f"Le livre '{
                  self.titre}' n'a pas été emprunté ou est déjà disponible.")


# Exemple d'utilisation :
livre1 = Livre("Harry Potter", "J.K. Rowling")
print("Le livre est disponible ?", livre1.verification())  # True

livre1.emprunter()  # Emprunter le livre
print("Le livre est disponible ?", livre1.verification())  # False

livre1.rendre()  # Rendre le livre
print("Le livre est disponible ?", livre1.verification())  # True
