class Aritmetica: 
    """ 
    clase aritmetica para realizar las operaciones sumar, restar, etc
    """
    def __init__(self,operandoA,operandoB): 
        self.operandoA = operandoA 
        self.operandoB = operandoB 
    
    def sumar(self): 
        return self.operandoA + self.operandoB 
    
    def restar(self): 
        return self.operandoA - self.operandoB 
    
    def dividir(self): 
        return self.operandoA / self.operandoB 
    
    def multiplicar(self): 
        return self.operandoA * self.operandoB 
    


aritmetica1=Aritmetica(5,3) 
print(f'multiplicacion:  {aritmetica1.multiplicar()}') 
print(f'suma:  {aritmetica1.sumar()}') 
print(f'resta:  {aritmetica1.restar()}') 
print(f'division:  {aritmetica1.dividir():.2f}') 
