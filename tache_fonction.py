class Tache:
    # Valeurs : nom, desc, temps, statut, membres, id_projet #
    def __init__(self, nom: str, desc: str, temps: int, statut: str, membres: list, id_projet: str):
        self.setNom(nom)
        self.setDesc(desc)
        self.setTemps(temps)
        self.setStatut(statut)
        self.membres = membres
        self.setID_projet(id_projet)

    def setNom(self, newName: str): # change le nom avec une valeur donné
        self.nom = newName

    def getNom(self): # récupère le nom de la tâche
        return self.nom
    
    def setDesc(self, newDesc: str): # change la description avec une valeur donné
        self.desc = newDesc

    def getDesc(self): # récupère la description de la tâche
        return self.desc
    
    def setTemps(self, newTemps: int): # change le temps avec une valeur donné
        self.temps = newTemps

    def getTemps(self): # récupère le temps de la tâche
        return self.temps
    
    def setStatut(self, newStatut: str): # change le statut avec une valeur donné
        validAnswers = ["pas commançé", "à faire", "en cours", "terminé"]
        newStatut = newStatut.lower()
        if newStatut in validAnswers:
            self.statut = newStatut
        else:
            print("Erreur : valeur invlide")

    def getStatut(self): # récupère le statut de la tâche
        return self.statut
    
    def addMembre(self, newMembre): # ajoute un membre avec une valeur donné
        self.membres.append(newMembre)

    def getMembres(self): # récupère les membres de la tâche
        return self.membres
    
    def remMembre(self, delMembre): # supprime un membre de la tâche
        self.membres.remove(delMembre)
    
    def setID_projet(self, newProjectID): # change l'id du projet associé avec une valeur donné
        self.id_projet = newProjectID

    def getID_projet(self): # récupère l'ID du projet associé à la tâche
        return self.id_projet