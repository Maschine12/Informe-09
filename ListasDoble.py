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

    def agregarUltimo(self, dato):
        if len(self) == 0:
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.sig = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.sig = Nodo(dato)
            self.ultimo.sig = self.primero

    
    # busca el nodo por dato
    def buscarNodo(self, dato):
        aux = self.primero
        existe = False
        while aux:
            if aux.dato == dato:
                existe = True
                break
            
            aux = aux.sig
            if aux.sig == self.primero.sig:
                break
        return existe

    #funcion para borar nodo 

    def eliminarNodo(self, dato):
        if self.buscarNodo(dato):
            actual   = self.primero
            anterior = self.primero
            while actual:
                if len(self) == 1:
                    self.primero = None
                    self.ultimo.sig = self.primero
                    break
                if actual.dato == dato:
                    if actual == self.primero:
                        self.primero = self.primero.sig
                        self.ultimo.sig = self.primero
                        
                    else:
                        anterior.sig = actual.sig
                    return
                anterior = actual
                actual = actual.sig
        else:
            raise Exception ("El Nodo no puede se eliminado por tratarse de un dato inexistente.")
    
    def eliminarPrimero(self,lista):
        datoEliminar = lista[0]
        self.eliminarNodo(datoEliminar)
    
    def eliminarUltimo(self,lista):
        nDatos = len(lista)
        datoEliminar = lista[nDatos-1]
        self.eliminarNodo(datoEliminar)
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


    





