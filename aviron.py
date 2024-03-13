class Bateau:
    def __init__(self, nom, vitesse):
        self.nom = nom
        self.vitesse = vitesse
        self.distance_parcourue = 0

    def avancer(self):
        self.distance_parcourue += self.vitesse / 2

    def __str__(self):
        return f"{self.nom},{self.distance_parcourue}"


class Bateau2x(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)


class BateauSkiff(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)


class Course:
    def __init__(self, type_bateau):
        self.type_bateau = type_bateau
        self.bateaux = []
        self.en_cours_course = False
        self.distance_max = 2000

    def ajout_bateau_ligne_depart(self, bateau):
        if isinstance(bateau, Bateau) and isinstance(bateau, eval(f'Bateau{self.type_bateau.capitalize()}')):
            self.bateaux.append(bateau)
        else:
            print("Le bateau n'a pas pu être ajouté.")

    def depart(self):
        self.en_cours_course = True

    def en_cours(self):
        return self.en_cours_course

    def next_loop(self):
        for bateau in self.bateaux:
            bateau.avancer()
        if all(bateau.distance_parcourue >= self.distance_max for bateau in self.bateaux):
            self.en_cours_course = False

    def affiche_positions(self):
        positions = ""
        for bateau in self.bateaux:
            positions += str(bateau) + "\n"
        return positions

    def vainqueur(self):
        if not self.en_cours_course:
            fastest_bateau = max(self.bateaux, key=lambda x: x.distance_parcourue)
            return f"Le vainqueur est {fastest_bateau.nom} avec une distance parcourue de {fastest_bateau.distance_parcourue}m."
        else:
            return "La course n'est pas terminée."


# Exemple d'utilisation
course_cadets = Course('2x')
bateau_1_2x = Bateau2x('Mickey', 62)
bateau_2_2x = Bateau2x('Minnie', 70)
bateau_3_skiff = BateauSkiff('Picsou', 120)

course_cadets.ajout_bateau_ligne_depart(bateau_1_2x)
course_cadets.ajout_bateau_ligne_depart(bateau_2_2x)
course_cadets.ajout_bateau_ligne_depart(bateau_3_skiff)

course_cadets.depart()

while course_cadets.en_cours():
    course_cadets.next_loop()
    print(course_cadets.affiche_positions())

print(course_cadets.vainqueur())
