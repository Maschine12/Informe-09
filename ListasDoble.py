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
            datoAuxiliar.siguiente = datoAuxiliar.siguiente= Nodo(dato)
            self.ultimoDato.siguiente=self.primeroLista
    


