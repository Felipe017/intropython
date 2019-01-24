class foton:
    def __init__(self, px = 0, py = 0):
            self.px = float(px) 
            self.py = float(py)

    def energia(self):
        # E^2 = P^2, onde P = sqrt(px^2 + py^2)
        return ((self.px**2 + self.py**2)**0.5)
    
    def tri_vet(self):
        tri_vet = [self.px, self.py, self.energia()] 
        return tri_vet