from pymongo import MongoClient
from _membre_create import membre_create
from projet_fonction import *
#conection to mongodb
try:
    client = MongoClient()
    print("Connected successfully!!!")
    db_list = client.list_database_names()
    print("Base de donnéer dispo: ",db_list)
except Exception as e:
    print("Could not connect to MongoDB" + e)

#Set up de la base de donnée   
db=client['Gestion_projets']

if db.membre.count_documents({}) == 0:
    for i in range(10):
        membre_create(db)
    print("Membres create")
# if db.projet.count_documents({}) == 0:
#     for i in range(5):
#         projet_create(db)
#     print("Projects create")

controlleur_ajouter_membre_projet(db,"projet1","nmiller@example.com")

