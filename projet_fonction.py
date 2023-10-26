from faker import Faker
# Description: Fonctions pour la gestion des projets
def projet_create(database):
    fake=Faker()
    # create database and collection    
    
    projet_collection=database['projet']

    shema_projet = {
        "Nom_projet":fake.company(),
        "description": fake.text(),
        "membre": [],
        "tache": [],
    }
    
    projet_collection.insert_one(shema_projet)

# Ajouter un projet à un membre
def add_projet_to_membre(database, nom, nom_projet):
    # Récupérer le document membre correspondant à l'id
    membre = database.membre.find_one({'Nom': nom})
    if membre is None:
        print("Membre non trouvé")
        return
    
    # Ajouter l'id du projet à la liste des projets associés au membre
    if nom_projet not in membre["Projet"]:
        database.membre.update_one({'Nom': nom}, {'$push': {"Projet": nom_projet}})
    else:
        print("Le projet "+nom_projet+ " est déjà associé au membre")
        return

    print("Le Projet "+ nom_projet + " a été ajouté au membre: "+nom+" avec succès")
    
def display_projet(database,name_projet=""):
    if name_projet != "":
        projet = database.projet.find({"Nom_projet":name_projet})
        print(projet +"\n"+ "Description: " + projet["description"])
    else:
        projets = database.projet.find()
        for projet in projets:
            print("Liste de tous les projets: "+projet)