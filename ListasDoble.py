class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig  = None
    
class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    #agrega elemento al inicio 

    def agregarInicio(self, dato):
        if len(self) == 0:
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.sig = self.primero
        else:
            aux = Nodo(dato)
            aux.sig = self.primero
            self.primero = aux
            self.ultimo.sig = self.primero
            
    # agrega elemento al final

    def agregarFinal(self,dato):
        if len(self) == 0:
            self.primeroLista=self.ultimoDato = Nodo(dato)
            self.ultimoDato.siguiente = self.primeroLista
        else:
            datoAuxiliar= self.ultimoDato
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
    

    def __len__(self):
        auxiliar = self.primeroLista
        contador = 0
        while auxiliar:
            contador += 1
            if auxiliar.siguiente == self.primeroLista:
                break
        return contador

    def __getitem__(self,indice):
        if indice >= 0 and indice < len(self):
            datoActual = self.primeroLista
            for i in range(indice):
                datoActual = datoActual.siguiente
            return datoActual.dato
        else:
            raise IndexError("indice fuera de rango")



if __name__ == "__main__":
    ListaC = Circular()
    ListaC.agregarInicio(3)
    ListaC.agregarFinal(2)
    ListaC.agregarInicio(1)
    print("Datos guardados  ")
    print(ListaC)


    # ListaC.reemplazarNodo(3,55)
    # ListaC.reemplazarNodo(2,89)
    # ListaC.reemplazarNodo(6,7982)
    # print("Datos modificados :")
    # print(ListaC)


    # ListaC.borarNodo(1)
    # print("Mostrar show ")
    # print(ListaC)


    





