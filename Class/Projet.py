class Projet:
    nom_projet = ""
    description = ""
    membre = []
    tache = []
    
    #constructor
    def __init__(self, nom_projet, description, membre, tache):
        self.nom_projet = nom_projet
        self.description = description
        self.membre = membre
        self.tache = tache
        
        # projet = {
        #     "nom_projet": self.nom_projet,
        #     "description": self.description,
        #     "membre": self.membre,
        #     "tache": self.tache
        # }
        
            
    #getters
    def get_nom_projet(self):
        return self.nom_projet
    def get_description(self):
        return self.description
    def get_membre(self):
        return self.membre
    def get_tache(self):
        return self.tache
    
    #setters
    def set_nom_projet(self, nom_projet):
        self.nom_projet = nom_projet
        
    def set_description(self, description):
        self.description = description
    
    def add_membre(self, membre):
        #membre_id
        self.membre.append(membre)
        
    
    
    