# Fichier de creation et options d'un participant


##########################################################################
##      CATEGORIE D'AGE ET DE POIDS (EN FONCTION DU GENRE) - BANK       ##
##########################################################################

age_class = [
    "EJ", "MP", "P", "B",
    "M", "C", "J", "S",
    "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11"
]

weights_F = [
    [-28, -32, -36, -40, -44, -48, -52, -57, -63, +63], # Categorie de poids Benjamines : B
    [-36, -40, -44, -48, -52, -57, -63, -70, +70], # Categorie de poids Minimes : MI
    [-40, -44, -48, -52, -57, -63, -70, +70], # Categorie de poids Cadettes : C
    [-44, -48, -52, -57, -63, -70, -78, +78], # Categorie de poids Juniors : J
    [-48, -52, -57, -63, -70, -78, +78], # Categorie de poids Seniors/Veterans : S/M?
]

weights_M = [
    [-26, -30, -34, -38, -42, -46, -50, -55, -60, -66, +66], # Categorie de poids Benjamins : B
    [-34, -38, -42, -46, -50, -60, -66, -73, -81, -81, +81], # Categorie de poids Minimes : MI
    [-46, -50, -55, -60, -66, -73, -81, -90, +90], # Categorie de poids Cadets : C
    [-55, -60, -66, -73, -81, -90, -100, +100], # Categorie de poids Juniors : J
    [-60, -66, -73, -81, -90, -100, +100], # Categorie de poids Seniors/Veterans : S/M?
]

# Table de tous les participants --- Pas l'ideal, mais on verra
all_Participants = []


###########################################################
##      INFORMATIONS PERSONNELLES DES PARTICIPANTS       ##
###########################################################

class Participant :
    
    def __init__(self, name, fname, gender, category, wClass) :
        self = self
        self.nom = name.upper()
        self.prenom = fname
        self.genre = gender.upper()
        self.categorie = category.upper()
        self.poids = -1*wClass

        # Ajout à la table de tous les participants - Ajout de l'adresse mémoire
        all_Participants.append(self)

    def getName(self) : return self.nom
    def getFName(self) : return self.prenom
    def getGender(self) : return self.genre

    def getCategory(self) : return self.categorie   # AGE : ATTENTION - REFAITE
    def getPositionClass(self) : return self.poids   # POIDS : ATTENTION - REFAITE

    # Override - getCtageory(self) - AGE
    def getAgeCategory(self) :
        self.categorie.upper()
        for i in (age_class) :
            if self.getCategory() == i : return i
            else : continue
        return "[ERREUR ENTREE]"

    def getWeightFeminine(self) :
        if self.genre == 'F' :
            if self.getCate() == "B":
                for i in weights_F[0] :
                    if i <= self.getClass() : return i
                return weights_F[0][-1]

            elif self.getCate() == "M":
                for i in weights_F[1] :
                    if i <= self.getClass() : return i
                return weights_F[1][-1]

            elif self.getCate() == "C":
                for i in weights_F[2] :
                    if i <= self.getClass() : return i
                return weights_F[2][-1]

            elif self.getCate() == "J":
                for i in weights_F[3] :
                    if i <= self.getClass() : return i
                return weights_F[3][-1]

            else :
                for i in weights_F[4] :
                    if i <= self.getClass() : return i
                return weights_F[4][-1]

        else : return "[ERREUR ENTRÉE]"

    def getWeightMasculin(self) :
        if self.genre == 'M' :
            if self.getCate() == "B":
                for i in weights_M[0] :
                    if i <= self.getClass() : return i
                return weights_M[0][-1]

            elif self.getCate() == "M":
                1+1
                for i in weights_M[1] :
                    if i <= self.getClass() : return i
                return weights_M[1][-1]

            elif self.getCate() == "C":
                1+1
                for i in weights_M[2] :
                    if i <= self.getClass() : return i
                return weights_M[2][-1]

            elif self.getCate() == "J":
                for i in weights_M[3] :
                    if i <= self.getClass() : return i
                return weights_M[3][-1]

            else :
                for i in weights_M[4] :
                    if i <= self.getClass() : return i
                return weights_M[4][-1]

        else : return "[ERREUR ENTRÉE]"

