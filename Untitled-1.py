class Nodo:
    def __init__(self,valor):
        self.dato=valor
        self.siguiente=None
        
class ListaSE:
    def __init__(self):
        self.cabeza=None
        
    def agregar_inicio(self,valor):
        nuevo_nodo=Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza=nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza=nuevo_nodo
    
    def agregar_final(self,valor):
        nuevo_nodo=Nodo(valor)
        
        if self.cabeza is not None:
            nodo=self.cabeza
            while nodo.siguiente!=None:
                nodo=nodo.siguiente
            nodo.siguiente=nuevo_nodo
            return
        else:
            self.cabeza=nuevo_nodo
            
    def eliminar_ultimo(self):
        if self.cabeza is not None:
            nodo=self.cabeza
            while nodo.siguiente!=None:
                nodo_anterior=nodo
                nodo=nodo.siguiente
            nodo_anterior.siguiente=None

        
        
            
lista_simple=ListaSE()
lista_simple.agregar_inicio(5)
print(lista_simple.cabeza.dato)    
lista_simple.agregar_inicio(8)    
print(lista_simple.cabeza.dato)  
            
        