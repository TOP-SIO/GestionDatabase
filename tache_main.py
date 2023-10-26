from pymongo import MongoClient # BDD Mongo Orienté document
from tache_fonction import Tache # tache_fonction.py, class Tache

def connection(): # essaye de se connecter à la BDD
    try:
        global client, db, collection
        client = MongoClient("localhost", 27017)
        db_list = client.list_database_names()
        db = client["Gestion_projets"]
        collection = db["Taches"]
        return ("Connexion réussie. Bases de données disponiles :", db_list)
    except Exception as e:
        return ("Erreur de connexion : {e}")

def createTask(nom, desc, temps, statut, membres, id_projet): # créer une tache dans la BDD
    TASK = {"nom": nom, "desc": desc, "temps": temps, "statut": statut, "membres": membres, "id_projet": id_projet}
    insert_tache = collection.insert_one(TASK)
    return insert_tache.inserted_id

def updateTask():
    TASK = {"nom": T.getNom(), "desc": T.getDesc(), "temps": T.getTemps(), "statut": T.getStatut(), "membres": T.getMembres(), "id_projet": T.getID_projet()}
    update_tache = collection.update_one({"nom": T.getNom()}, {"$set": TASK})
    return update_tache.acknowledged

T = Tache("TÂCHE", "LA DESCRIPTION", 88888888, "à faire", ["Personne 1", "Personne 2", "Personne 3"], None)
print(connection())
"""Créer une tâche"""
# print(createTask(T.getNom(), T.getDesc(), T.getTemps(), T.getStatut(), T.getMembres(), T.getID_projet()))
"""Mettre à jour une tâche"""
# print(updateTask())