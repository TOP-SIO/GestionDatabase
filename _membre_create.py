from faker import Faker
from pymongo import MongoClient

def membre_create(database):
    
    fake=Faker()
    membre_collection=database['membre']
    membre = {
        "Nom":fake.last_name(),
        "Prenom":fake.first_name(),
        "Mail": fake.email(),
        "Poste": fake.job(),
        "Projet": [],
        "Tache": []
        
    }
    membre_collection.insert_one(membre)
            
            

            
                

