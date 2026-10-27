# Fichier de creation et options d'un participant
from datetime import *

##########################################################################
##      CATEGORIE D'AGE ET DE POIDS (EN FONCTION DU GENRE) - BANK       ##
##########################################################################

age_class = [
    "EJ", "MP", "P", "B",
    "M", "C", "J", "S",
    "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11"
]

weights_F = [
    [28, 32, 36, 40, 44, 48, 52, 57, 63], # Categorie de poids Benjamines : B
    [36, 40, 44, 48, 52, 57, 63, 70], # Categorie de poids Minimes : M
    [40, 44, 48, 52, 57, 63, 70], # Categorie de poids Cadettes : C
    [44, 48, 52, 57, 63, 70, 78], # Categorie de poids Juniors : J
    [48, 52, 57, 63, 70, 78], # Categorie de poids Seniors/Veterans : S/V?
]

weights_M = [
    [26, 30, 34, 38, 42, 46, 50, 55, 60, 66], # Categorie de poids Benjamins : B
    [34, 38, 42, 46, 50, 60, 66, 73, 81, 81], # Categorie de poids Minimes : MI
    [46, 50, 55, 60, 66, 73, 81, 90], # Categorie de poids Cadets : C
    [55, 60, 66, 73, 81, 90, 100], # Categorie de poids Juniors : J
    [60, 66, 73, 81, 90, 100], # Categorie de poids Seniors/Veterans : S/M?
]

# Table de tous les participants --- Pas l'ideal, mais on verra
all_Participants = []


###########################################################
##      INFORMATIONS PERSONNELLES DES PARTICIPANTS       ##
###########################################################

class Participant :

    def __init__(self, name = "nom", fname = "prenom", gender = "genre", club = "club", birth = "annee de naissance", weight = "poids") :
        self = self
        self.nom = name.upper()
        self.prenom = fname.capitalize()
        self.genre = gender.upper()
        self.club = club.upper()
        self.annee = birth
        self.poids = weight

        all_Participants.append(self)    # Ajout à la table de tous les participants - Ajout de l'adresse mémoire

    def toString(self) : return f"Nouvelle inscription : {self.getName()} {self.getFName()} - {self.getGender()}.{self.getCategory()}.{self.getWeightClass()}"
    def describe(self) : print(f"Nouvelle inscription : {self.getName()} {self.getFName()} - {self.getGender()}.{self.getCategory()}.{self.getWeightClass()}")
    def getName(self) : return self.nom
    def getFName(self) : return self.prenom
    def getGender(self) : return self.genre
    def getClub(self) : return self.club

    def getCategory(self) :
        current_y = datetime.now().year
        delta = current_y - self.annee

        if delta <= 5 : return "EJ"     # EJ
        elif 6 <= delta <= 7 : return "MP"     # MP
        elif 8 <= delta <= 9 : return "P"     # P
        elif 10 <= delta <= 11 : return "B"     # B
        elif 12 <= delta <= 13 : return "M"     # M
        elif 14 <= delta <= 16 : return "C"     # C
        elif 17 <= delta <= 19 : return "J"     # J
        elif 20 <= delta <= 30 : return "S"     # S

        for i in range(11) :
            if (30 + (i*5)) <= delta <= (35 + (i*5)) :
                return f"M{1+i}"     # M1-M11

    def getWeightClass(self) :
        for i in range(len(age_class)) :
            if age_class[i] == self.getCategory() :
                if i >= 4 : i = 4
                if self.getGender() == "F" :
                    for j in range(len(weights_F)) :
                        if self.poids <= weights_F[i][j] : return f"-{weights_F[i][j]}"
                    return f"+{weights_F[i][j]}"

                else :
                    for j in range(len(weights_M)) :
                        if self.poids <= weights_M[i][j] : return f"-{weights_M[i][j]}"
                    return f"+{weights_M[i][j]}"


############################################
##      TRI ET FILTRES PAR CRITERES       ##
############################################


    def filterByGender(self, gender) :
        gender_targeted = []
        for i in all_Participants :
            if i.getGender() == gender :
                gender_targeted.append(i)
        return gender_targeted

    def filterByCategory(self, cate) :
        category_targeted = []
        for i in all_Participants :
            if i.getCategory() == cate :
                category_targeted.append(i)
        return category_targeted

    def filterByWeightClass(self, weightClass) :
        weightClass_targeted = []
        for i in all_Participants :
            if i.getWeightClass() == weightClass :
                weightClass_targeted.append(i)
        return weightClass_targeted

    def filterByClub(self, club) :
        all_clubs = []
        clubs = {}

        for i in all_Participants :                     # Reperage et remplissage de tous les clubs
            if i.getClub() not in all_clubs :
                all_clubs.append(i.getClub())
        for i in all_clubs :                            # Initialisation des tables de participant par club, dans le dico des clubs
            clubs[i] = []
        for i in clubs.keys() :                         # Remplissage des tables de participants par clubs, en appelant les cles du dico
            for j in all_Participants :
                if i == j.getClub() :
                    clubs.get(i).append(j)
        for i in clubs.keys() :                         # Recherche et retour du club cible
            if i == club.upper() :
                return clubs.get(i)

