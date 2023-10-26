from pymongo import MongoClient # BDD Mongo Orienté document
from tache_fonction import Tache # tache_fonction.py, class Tache

def connection(): # essaye de se connecter à la BDD
    try:
        global client
        client = MongoClient("localhost", 27017)
        db_list = client.list_database_names()
        return ("Connexion réussie. Bases de données disponiles :", db_list)

    except Exception as e:
        return ("Erreur de connexion : {e}")

def createTask(nom, desc, temps, statut, membres, id_projet): # créer une tache dans la BDD
    TASK = {"nom": nom, "desc": desc, "temps": temps, "statut": statut, "membres": membres, "id_projet": id_projet}
    global collection
    db = client["Gestion_projets"]
    collection = db["Taches"]
    insert_tache = collection.insert_one(TASK)
    return insert_tache.inserted_id

T = Tache("TÂCHE", "LA DESCRIPTION", 88888888, "à faire", ["Personne 1", "Personne 2", "Personne 3"], None)
print(connection())
print(createTask(T.getNom(), T.getDesc(), T.getTemps(), T.getStatut(), T.getMembres(), T.getID_projet()))
