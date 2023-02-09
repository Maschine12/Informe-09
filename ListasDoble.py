class Nodo:
    def __init__(self,dato):
        self.dato =dato
        self.siguiente = None
    
class Circular:
    def __init__(self):
        self.primeroLista = None
        self.ultimoDato = None

    def agregarInicio(self,dato):
        if len(self)==0:
            self.primeroLista = self.ultimoDato = Nodo(dato)
            self.ultimoDato.siguiente=self.primeroLista
        else:
            datoAuxiliar= Nodo(dato)
            datoAuxiliar.siguiente = self.primeroLista
            self.ultimoDato.siguiente = self.primeroLista
    def agregarFinal(self,dato):
        if len(self) == 0:
            self.primeroLista=self.ultimoDato = Nodo(dato)
            self.ultimoDato = self.primeroLista
        else:
            datoAuxiliar= Nodo(dato)
            self.ultimoDato = datoAuxiliar.siguiente= Nodo(dato)
            self.ultimoDato.siguiente=self.primeroLista
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

    

    