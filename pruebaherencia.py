from pruebaobjetos import * 

class dueño(carro): 
    def __init__(self, marca, color,nombreDueño):
        super().__init__(marca, color) 
        self.nombreDueño=nombreDueño 
    
    def __str__(self): 
        return f'{super().__str__()} Dueño: {self.nombreDueño}' 


