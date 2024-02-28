class Nodo:
    def __init__(self,valor):
        self.dato=valor
        self.siguiente=None
        
class ListaSE:
    def __init__(self):
        self.cabeza=None
        
    def verificar_vacio(self):
        if(self.cabeza is None):
            return True
        else:
            return False
        
    def contar_nodos(self):
        nodo = self.cabeza
        count = 0
        while nodo != None:
            count+=1
            nodo = nodo.siguiente
            
        return count
    
    def buscar_nodo(self, valor):
        nodo = self.cabeza
        while nodo != None:
            if(nodo.dato==valor):
                return True
            nodo = nodo.siguiente
        return False
    
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

        
    def eliminar_inicio(self):
        self.cabeza = self.cabeza.siguiente
        
    
        
            
lista_simple=ListaSE()

#Agregar elementos de prueba iniciales
lista_simple.agregar_inicio(5)
lista_simple.agregar_final("hola")
lista_simple.agregar_inicio(8)    

#Comprobar metodos de busqueda y conteo
print(lista_simple.contar_nodos())
print(lista_simple.buscar_nodo("hola")) ##Tiene que devolver True
print(lista_simple.buscar_nodo("a")) ##Tiene que devolver False

#Comprobar metodo de eliminacion del inicio
lista_simple.eliminar_inicio() ##Se elimina el nodo con valor 8
print("Luego de la eliminacion del primero quedan ",lista_simple.contar_nodos()," nodos")

#Comprobar metodo eliminacion del ultimo
lista_simple.agregar_final("AAAA")
lista_simple.agregar_final("EEEE") ##Aqui hay 4 elementos en la lista
lista_simple.eliminar_ultimo() ##Se elimina el nodo con valor EEEE
print("Luego de la eliminacion del ultimo quedan ",lista_simple.contar_nodos()," nodos")
print(lista_simple.buscar_nodo("EEEE")) ##Tiene que devolver False
            
        