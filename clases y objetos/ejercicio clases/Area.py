class Area: 
    def __init__(self, base, altura) :
        self.base = base 
        self.altura= altura 
    def area(self): 
        return self.base * self.altura  
    


base=float(input('Digite la base: ')) 
altura=float(input('Digite la altura: ')) 

area1=Area(base,altura)  
print(f"area: {area1.area():.2f}") 

base=float(input('Digite la base: ')) 
altura=float(input('Digite la altura: '))  

area2=Area(base,altura)
print(f"area: {area2.area():.2f}")
