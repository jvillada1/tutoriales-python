from dispositivoEntrada import dispositivoEntrada
class Raton(dispositivoEntrada):  
    contadorRatones=0 
    def __init__(self,nombre,tipoEntrada):
        dispositivoEntrada.__init__(self,tipoEntrada,nombre)
        Raton.contadorRatones +=1 
        self._id_raton=Raton.contadorRatones 
    
    def __str__(self):
        return f'{super().__str__()} id raton: {self._id_raton}' 



if __name__=='__main__': 
    raton1=Raton('lenovo','mouse') 
    print(raton1)  
    raton2=Raton('mouse','razer') 
    print(raton2)