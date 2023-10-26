class Membre :
    """Classe Membre"""
    nom = ""
    prenom = ""
    mail = ""
    poste = ""
    projet = []
    tache = []
    
    def __init__(self, nom, prenom, mail, poste, projet, tache):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.poste = poste
        self.projet = projet
        self.tache = tache
    
    #getters
    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
    
    def get_mail(self):
        return self.mail
    
    def get_poste(self):
        return self.poste
    
    def get_projet(self):
        return self.projet
    
    def get_tache(self):
        return self.tache