class Particula:
    def __init__(self, px = 0, py = 0, m = 0):
            self.px = float(px) 
            self.py = float(py)
            self.m = float(m)
    def energia(self):
        # E^2 = m^2 + P^2, onde P = sqrt(px^2 + py^2)
        return (((self.m)**2 + self.px**2 + self.py**2)**0.5)
    
    def tri_vet(self):
        tri_vet = [self.px, self.py, self.energia()] 
        return tri_vet

class eletron(Particula): 
    """ Classe que representa o eletron, que é um tipo particula"""
    def __init__(self, px = 0, py = 0, m = 0.511):#a massa do elétron é de 0.511 MeV
        super().__init__(px,py,m)

class foton(Particula):
    """ Classe que representa o foton, que é um tipo particula"""
    def __init__(self, px = 0, py = 0, m = 0):
        #Forma de chamar o inicializador da classe basse
        super().__init__(px,py,m)
        
