class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0  # nombre de crédits par défaut à zéro
        # attribut level qui prend la valeur de la méthode studentEval
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        # Ajoute un nombre de crédits au total de l'étudiant
        if credits > 0:
            self.__credits += credits
            print(f"{credits} crédits ajoutés avec succès.")
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")

    def __student_eval(self):
        # Méthode privée pour évaluer le niveau de l'étudiant en fonction du nombre de crédits
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        # Affiche les informations de l'étudiant
        print(f"Nom = {self.__nom}  Prénom = {self.__prenom}  id = {
              self.__numero_etudiant} Niveau = {self.__level}")


# Instanciation de l'étudiant John Doe avec le numéro d'étudiant 145
john_doe = Student("John", "Doe", 145)

# Ajout des crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)

# Affichage des informations de l'étudiant
john_doe.student_info()
