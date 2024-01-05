class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  # attribut privé reservoir initialisé à 50 par défaut

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def set_en_marche(self, nouvel_etat):
        self.__en_marche = nouvel_etat

    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir

    # Méthode privée pour vérifier si le réservoir est suffisamment plein pour démarrer
    def __verifier_plein(self):
        return self.__reservoir > 5

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer : le réservoir est trop faible.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")


# Exemple d'utilisation :
ma_voiture = Voiture("Toyota", "Corolla", 2020, 25000)

# Accès aux attributs via les assesseurs (getters)
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("En marche ?", ma_voiture.get_en_marche())
print("Reservoir :", ma_voiture.get_reservoir())

# Modification d'attributs via les mutateurs (setters)
ma_voiture.set_kilometrage(27000)
ma_voiture.set_reservoir(10)

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()
