class  Particula :
   
    def  __init__ ( self ,  m = 0, p = 0): 
       
        self.m = float(m)
        self.p = float(p) 

    def energia (self):

	#E=((m*c**2)**2+(p*c)**2)**0.5
        return ((self.m)**2+(self.p)**2)**0.5

    def quad_vet (self):
        quad_vet= [self.p, self.energia()] 
        return quad_vet 

