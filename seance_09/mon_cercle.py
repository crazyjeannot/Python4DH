from math import *
from matplotlib import pyplot as plt

class CCircle:
    def __init__(self,a,b,r):
        self.coord_a = a
        self.coord_b = b
        self.rayon = r

    def perimetre(self):
        return 2*pi*self.rayon
    
    def surface(self):
        return pi*self.rayon**2
    
    def equation_cercle(self,x,y):
        return (x - self.coord_a)**2 + (y - self.coord_b)**2 - self.rayon**2
    
    def appartenance(self,x,y):
        if (self.equation_cercle(x,y) == 0):
            print("le point ",x,y," appartient au cercle")
        else:
            print("le point ",x,y," n'appartient pas au cercle")
    
    def afficher_centre(self):
        plt.figure(figsize=(10,8))
        plt.subplot(1,1,1)
        plt.scatter(self.coord_a, self.coord_b)
        
    def draw(self):
        fig, ax = plt.subplots()
        ax.set(xlim=(-20,20), ylim=(-20,20))
        circle1 = plt.Circle((self.coord_a, self.coord_b), self.rayon)
        ax.add_artist(circle1)
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    