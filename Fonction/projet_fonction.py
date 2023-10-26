from math import e
from faker import Faker
from Class.Projet import Projet

#CRUD projet
def controlleur_creer_projet (database,nom_projet, description, membre, tache):
    try:
        new_projet = Projet(nom_projet, description, membre, tache)
        projet = {
                "nom_projet": new_projet.get_nom_projet(),
                "description": new_projet.get_description(),
                "membre": new_projet.get_membre(),
                "tache": new_projet.get_tache()
            }
        projet_collection=database['projet']
        projet_collection.insert_one(projet)
    except Exception as e:
        print("Erreur: ",e)

def controlleur_afficher_projet(database,nom_projet):
    try:
        projet=database.projet.find_one({"nom_projet":nom_projet})
        membres=database.membre.find({"_id": {"$in": projet["membre"]}})
        
        if projet is None:
            print("Projet non trouvé")
            return
        
        print("Nom du projet: ",projet["nom_projet"],
            "\nDescription: ",projet["description"],
            "\nMembres: ",[membre["Mail"] for membre in membres],
            "\nTaches: ",projet["tache"])
        
    except Exception as e:
        print("Erreur: ",e)
        
    

#CRUD membre projet
def controlleur_ajouter_membre_projet(database,nom_projet,mail_membre):
    projet=database.projet.find_one({"nom_projet":nom_projet})
    membre=database.membre.find_one({"Mail":mail_membre})
    projet_id = projet["_id"]
    if projet is None:
        print("Projet non trouvé")
        return
    if membre is None:
        print("Membre non trouvé")
        return
    
    id_membre=membre["_id"]
    
    projet_collection=database['projet']
    projet_collection.update_one({"nom_projet":nom_projet},{'$push': {"membre": id_membre}})

def controlleur_supprimer_membre_projet(database,nom_projet,mail_membre):
    projet=database.projet.find_one({"nom_projet":nom_projet})
    membre=database.membre.find_one({"Mail":mail_membre})
    if projet is None:
        print("Projet non trouvé")
        return
    if membre is None:
        print("Membre non trouvé")
        return
    
    id_membre=membre["_id"]
    
    projet_collection=database['projet']
    projet_collection.update_one({"nom_projet":nom_projet},{'$pull': {"membre": id_membre}})