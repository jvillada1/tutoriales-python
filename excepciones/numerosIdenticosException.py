#definicion de excepciones personalizadas 
class numerosIdenticosException(Exception): 
    
    def __init__(self,mensaje) : #se sobreescribe el metodo init de Exception 
        self.message=mensaje 
        