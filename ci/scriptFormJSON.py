import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

errors_raised = []


def check_struct(file = "nom_du_fichier") :
    with open(file, "r", encoding = "utf-8") as js :
        data = json.loads(js.read())
        entries_expected = ["Nom", "Prenom", "Genre", "Club", "Categorie", "Positionnement"]

        for i in range(len(data)) :
            for j in range(len(entries_expected)) :
                if entries_expected[j] not in data[i] :
                    errors_raised.append(f"Champs {entries_expected[j]} manquant - Element n.{i + 1}")

def check_errors() :
    if (len(errors_raised) > 0) : 
        print(f"{len(errors_raised)} erreurs detectees ! :\n\n")
        for i in range(len(errors_raised)) :
            print(f"\t{errors_raised[i]}")
    else : print("\nRien à signaler !\n")
    print("-----------------------------------------------------")

def scripting() :
    check_struct(BASE.parent / "backSupport" / "data.json")
    check_errors()



scripting()