from faker import Faker
from pymongo import MongoClient
from Class.Membre import Membre

def controlleur_creer_membre(database, nom, prenom, mail, poste, projet, tache):
    try:
        new_membre = Membre(nom, prenom, mail, poste, projet, tache)
        membre = {
            "nom": new_membre.get_nom(),
            "prenom": new_membre.get_prenom(),
            "mail": new_membre.get_mail(),
            "poste": new_membre.get_poste(),
            "projet": new_membre.get_projet(),
            "tache": new_membre.get_tache()
            
        }
        membres_collection = database["membres"]
        membres_collection.insert_one(membre)
    except Exception as e:
        print("Erreur: ", e)
    

            

            
                

