# Fichier de gestion des donnees
import json
import participants


###################################################
##      GESTION DES DONNEES DE L'EVENEMENT       ##
###################################################


json_path = "backSupport/data.json"
json_reciever = "backSupport/recievePy.json"
json_participants = "backSupport/data.json"


class Manager :
    def __init__(self):
        pass


    def jsonToPy(self) :
        with open(json_path) as datas :     # Independantiser le fichier de lecture
            data = json.loads(datas.read())
        return data
    
    def pyToJson(self, datas) :     # Independantiser le fichier d'ecriture
        data = []
        data.append(datas)
        with open(json_reciever, "w") as rec :
            json.dump(data, rec)
        
    def addParticipant(self, name, fname, gender, category, wClass) :
        data = {
            "Nom" : f"{name}",
            "Prenom" : f"{fname}",
            "Genre" : f"{gender}",
            "Categorie d'age" : f"{category}",
            "Positionnement" : f"{wClass}",
        }; return data

