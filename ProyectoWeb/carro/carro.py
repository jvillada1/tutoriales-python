class Carro: 
    def __init__(self,request): 
        self.request=request #aqui vamos a almacenar la peticion 
        self.session=request.session #guardamos la sesion 
        carro=self.session.get("carro") 
        #se tiene que igualar la sesion del usuario con su carro 
        if not carro: 
            #se va a trabajar con diccionarios para poder ver los productos 
            carro=self.session["carro"]={} #si no hay carro, se crea con el diccionario vacio
        else: 
            self.carro=carro #si si hay carro, se dice que va a ser igual al que ya habia 
        
    def agregar(self,producto):  #vamos a hacer la funcion agregar 
        #primero se debe de comprobar que el producto a ingresar, no esté ya agregado 
        if(str(producto.id)not in self.carrro.keys()): #si no está el id, que lo cree y llene todo el diccionario con los datos del producto ingresado
            self.carro[producto.id]={"producto_id":producto.id, 
                                    "nombre":producto.nombre, 
                                    "precio":str(producto.precio), 
                                    "cantidad":1, 
                                    "imagen":producto.imagen.url,} 
        else: #en el caso de que si esté en el carro, se hace lo siguiente
            for key,value in self.carro.items():# se debe de recorrer y comprobar si la clave es igual a la que vamos a ingresar para que se sumen 
                if key==str(producto.id): 
                    value["cantidad"]=value["cantidad"]+1 #si lo encuentra, que le sume 1 al valor ya existente 
                    break #el break es para que si ya encuentra uno con el mismo id, que no recorra el resto de elementos 
        self.guardar_carro() #se va a llamar a una funcion que guardara el carro en la sesion 
                

    def guardar_carro(self): #se encarga de guardar los cambios realizados en el carro
        self.session["carro"]=self.carro 
        self.session.modified=True # que se pueda modificar la sesion 

    def eliminar(self,producto): #en la funcion eliminar lo que vamos a hacer es eliminar todo el producto del carro sin importar sus unidades, todas se borran 
        producto.id=str(producto.id) #primero para poder manejar el id, se debe de almacenar 
        if producto.id in self .carro: 
            del self.carro[producto.id] #si ese id está en el carro, que lo elimine de ahi
            self.guardar_carro() #se actualiza el carro con la sesion 

    def restar_producto(self,producto): #la funcion restar e va anecargar de restarle una unidad a los productos que se encuentren en el carro
        for key,value in self.carro.items():# se debe de recorrer y comprobar si la clave es igual a la que vamos a ingresar para que se sumen 
                if key==str(producto.id): 
                    value["cantidad"]=value["cantidad"]-1 #hace lo mismo de agregar pero en vez de sumar, resta 1 
                    if value["cantidad"]<1: #esta se comprobacion trata de que si las unidades que quedan son iguales a 1, que llame a la funcion eliminar
                        self.eliminar(producto)
                    break  
        self.guardar_carro() 
        
    def limipar_carro(self): #esta funcion se hace para cuando la persona quiera vaciar todo el carro
        self.session["carro"]={} 
        self.session.modified=True