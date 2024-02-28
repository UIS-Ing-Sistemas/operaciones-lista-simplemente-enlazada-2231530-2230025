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
        nodo=self.cabeza
        
        while nodo.siguiente!=None:
            pass
        
        
            
lista_simple=ListaSE()
lista_simple.agregar_inicio(5)
print(lista_simple.cabeza.dato)    
lista_simple.agregar_inicio(8)    
print(lista_simple.cabeza.dato)  
            
        