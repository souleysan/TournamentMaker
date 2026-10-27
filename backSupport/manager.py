# Fichier de gestion des donnees
import json
import participants


###################################################
##      GESTION DES DONNEES DE L'EVENEMENT       ##
###################################################


json_path = "backSupport/data.json"


class Manager :
    def __init__(self):
        pass


    def jsonToPy(self, file = "nom_du_Fichier_sans_extension") :
        with open(json_path) as datas :     # Independantiser le fichier de lecture
            data = json.loads(datas.read())
        return data

    def pyToJson(self, datas = "donnees_a_ecrire", file = "nom_du_Fichier_sans_extension") :
        data = []
        data.append(datas)
        with open(f"backSupport/{file}.json", "w") as rec :
            json.dump(data, rec)
        
    def setParticipant(self, name, fname, gender, category, wClass) :
        data = {
            "Nom" : f"{name}",
            "Prenom" : f"{fname}",
            "Genre" : f"{gender}",
            "Categorie d'age" : f"{category}",
            "Positionnement" : f"{wClass}",
        }; return data

