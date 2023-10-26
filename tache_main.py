from pymongo import MongoClient # BDD Orienté document
from tache_fonction import Tache # tache_fonction.py, class Tache

def connection():
    try:
        global client
        client = MongoClient("localhost", 27017)
        db_list = client.list_database_names()
        return ("Connexion réussie. Bases de données disponiles :", db_list)

    except Exception as e:
        return ("Erreur de connexion : {e}")
    
db = client["Gestion_projets"]

def createTask(nom, desc, temps, statut, membres, id_projet):
    TASK = {"nom": nom, "desc": desc, "temps": temps, "statut": statut, "membres": membres, "id_projet": id_projet}
    global collection
    collection = db["Taches"]
    insert_tache = collection.insert_one(TASK)
    return insert_tache.inserted_id

T = Tache("TÂCHE", "LA DESCRIPTION", 88888888, "à faire", ["Personne 1", "Personne 2", "Personne 3"], None)
print(connection())
print(createTask(T.getNom(), T.getDesc(), T.getTemps(), T.getStatut(), T.getMembres(), T.getID_projet()))
