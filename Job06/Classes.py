class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # dictionnaire pour représenter les plats commandés
        self.__statut_commande = "en cours"  # statut initial de la commande

    def ajouter_plat(self, nom_plat, prix_plat):
        # Ajoute un plat à la commande avec son prix et le statut de la commande
        self.__plats_commandes[nom_plat] = {
            'prix': prix_plat, 'statut': self.__statut_commande}
        print(f"Plat '{nom_plat}' ajouté à la commande.")

    def annuler_commande(self):
        # Annule la commande en changeant son statut
        self.__statut_commande = "annulée"
        print("La commande a été annulée.")

    def __calculer_total(self):
        # Calcule le total de la commande en privé
        total = sum(plat['prix'] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        # Affiche la commande avec son total à payer
        print(f"Commande numéro {self.__numero_commande}:")
        print("Plats commandés:")
        for nom_plat, details_plat in self.__plats_commandes.items():
            print(
                f"- {nom_plat}: {details_plat['prix']} € ({details_plat['statut']})")
        total = self.__calculer_total()
        print(f"Total à payer : {total} €")

    def calculer_TVA(self, taux_TVA):
        # Calcule la TVA en fonction du taux spécifié
        total = self.__calculer_total()
        tva = total * (taux_TVA / 100)
        print(f"TVA à {taux_TVA}% : {tva} €")


# Exemple d'utilisation :
commande1 = Commande("CMD001")

commande1.ajouter_plat("Pizza", 12.50)
commande1.ajouter_plat("Salade", 8.75)

commande1.afficher_commande()

commande1.calculer_TVA(20)

commande1.annuler_commande()
