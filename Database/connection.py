from pymongo import MongoClient

def connection():
    try:
        client = MongoClient()
        print("Connected successfully!!!")
        db_list = client.list_database_names()
        print("Base de donnéer dispo: ",db_list)
        database = client['Gestion_projets']
        return database
    except Exception as e:
        print("Erreur: ",e)
    
    