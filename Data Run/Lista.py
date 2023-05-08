from Nodo import Nodo

class Lista:

    def __init__ (self):
        self.raiz = None
        self.cola = None
        self.tam = 0

    def agregarNodo (self, dato):
        nuevo = Nodo(dato)
        if self.raiz == None:
            self.raiz = nuevo
        else:
            self.cola.next = nuevo
        self.cola = nuevo
        self.tam += 1
    
    def obtenerNodo (self, ind):
        if ind > self.tam:
            return None
        else:
            nodo = self.raiz
            for i in range (ind):
                nodo = nodo.next
            return nodo
        
class ListaCircular:
    
    def __init__ (self):
        self.raiz = None
        self.cola = None
        self.tam = 0

    def agregarNodo (self, dato):
        nuevo = Nodo(dato)
        if self.raiz == None:
            self.raiz = nuevo
        else:
            self.cola.next = nuevo
        self.cola = nuevo
        self.cola.next = self.raiz
        self.tam += 1
    
    def obtenerNodo (self, ind):
        nodo = self.raiz
        for i in range (ind):
            nodo = nodo.next
        return nodo