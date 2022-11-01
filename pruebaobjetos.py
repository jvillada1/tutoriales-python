class carro: 
    def __init__(self,marca,color): 
        self.marca=marca 
        self.color=color 
    
    def pintar(self,pintura): 
        self.color=pintura 
        return f'Su nuevo color es {pintura}' 
    
    def __str__(self): 
        return f'Marca: {self.marca}, color: {self.color}'

if __name__=='__main__': 
    carro1=carro('renault','blanco') 
    print(carro1) 
    carro1.pintar('amarillo') 
    print(carro1)