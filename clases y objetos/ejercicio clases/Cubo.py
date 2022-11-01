class Cubo: 
    def __init__(self,ancho,alto,profundo):
        self.ancho=ancho 
        self.profundo= profundo 
        self.alto = alto 
    
    def areaCubo(self):  
        return self.ancho * self.profundo *self.alto 

ancho= float(input("digite el ancho: ")) 
alto= float(input("digite el alto: "))
profundo= float(input("digite el profundo: "))

cubo1=Cubo(ancho,alto,profundo) 

print(f"el area del cubo es {cubo1.areaCubo():.2f}") 

ancho= float(input("digite el ancho: ")) 
alto= float(input("digite el alto: "))
profundo= float(input("digite el profundo: ")) 

cubo2=Cubo(ancho,alto,profundo)

print(f"el area del cubo es {cubo2.areaCubo():.2f}")
