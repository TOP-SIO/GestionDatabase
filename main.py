from pymongo import MongoClient
from faker import Faker
from Database.connection import connection
from Fonction.projet_fonction import *
from Fonction.membre_fonction import *
#conection to mongodb

db=connection()
fake = Faker()

if db.membre.count_documents({}) == 0:
    for i in range(10):
        controlleur_creer_membre(db,fake.last_name(), fake.first_name(), fake.email(), fake.job(),[],[])
if db.projet.count_documents({}) == 0:
    for i in range(3):
        controlleur_creer_projet(db,"projet"+str(i), fake.text(), [], [])

controlleur_afficher_projet(db,"projet1")

