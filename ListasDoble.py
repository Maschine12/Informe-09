class Nodo:
    def __init__(self,dato):
        self.dato =dato
        self.siguiente = None
    
class Circular:
    def __init__(self):
        self.primeroLista = None
        self.ultimoDato = None

    #agrega elemento al inicio 

    def agregarInicio(self,dato):
        if len(self)==0:
            self.primeroLista = self.ultimoDato = Nodo(dato)
            self.ultimoDato.siguiente=self.primeroLista
        else:
            datoAuxiliar= Nodo(dato)
            datoAuxiliar.siguiente = self.primeroLista
            self.ultimoDato.siguiente = self.primeroLista
            
            
    
    # agrega elemento al final

    def agregarFinal(self,dato):
        if len(self) == 0:
            self.primeroLista=self.ultimoDato = Nodo(dato)
            self.ultimoDato = self.primeroLista
        else:
            datoAuxiliar= Nodo(dato)
            self.ultimoDato = datoAuxiliar.siguiente= Nodo(dato)
            self.ultimoDato.siguiente=self.primeroLista

    
    # busca el nodo por dato
    def buscarNodo(self, dato):
        datoAuxiliar = self.primeroLista
        existe = False
        while datoAuxiliar:
            if datoAuxiliar.dato == dato:
                existe = True
                break
            datoAuxiliar = datoAuxiliar.siguiente
            if datoAuxiliar.siguiente == self.primeroLista:
                break
        return existe


    #Reemplaza el nodo datos cambiaras , dato nuevo

    def reemplazarNodo(self,datoCambiaré,nuevoDato):
        if self.buscarNodo(datoCambiaré):
            datoAux = self.primeroLista
            while datoAux:
                if datoAux.dato ==nuevoDato:
                    datoAux.dato = nuevoDato
                    break
                datoAux = datoAux.siguiente
                if datoAux.siguiente == self.primeroLista.siguiente:
                    break
        else:
            raise Exception("El dato para reemplaza no existe en la lista")

    #funcion para borar nodo 

    def borarNodo(self,datoBorar):
        if self.buscarNodo(datoBorar):
            dato1 = self.primeroLista
            dato2 = self.primeroLista
            while dato1:
                if len(self)==1:
                    self.primeroLista = None
                    self.ultimoDato.siguiente = self.primeroLista
                    break
                if dato1.dato== datoBorar:
                    if dato1 == self.primeroLista:
                        self.primeroLista = self.primeroLista.siguiente
                        self.ultimoDato.siguiente=self.primeroLista
                    else:
                        dato2.siguiente = dato1.siguiente
                    return
                dato2 = dato1
                dato1 = dato1.siguiente
            
        else:
            raise Exception("No se puede borar el nodo")
    

    def __str__(self) -> str:
        elementoAuxiliar = self.primeroLista
        elementos = ""
        while elementoAuxiliar:
            elementos += str(elementoAuxiliar.dato) + " "

            elementoAuxiliar = elementoAuxiliar.siguiente
            if elementoAuxiliar.siguiente == self.primeroLista.siguiente:
                break
            return elementos
    
    
    





