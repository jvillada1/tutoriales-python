from dispositivoEntrada import dispositivoEntrada
class teclado(dispositivoEntrada): 
    contador_teclados=0 
    def __init__(self, marca,tipoEntrada):
        teclado.contador_teclados +=1
        super().__init__(tipoEntrada, marca) 
        self._id_teclado = teclado.contador_teclados 
    
    def __str__(self):
        return f'{super().__str__()} id teclado: {self._id_teclado}' 
    

if __name__=='__main__': 
    teclado1=teclado('teclado','dell') 
    print(teclado1) 
    teclado2=teclado('teclado','asus' ) 
    print(teclado2)