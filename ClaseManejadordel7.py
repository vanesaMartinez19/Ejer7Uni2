from ClaseViajeroFrecuentedel7 import ViajeroFrecuente


class Manejador:
    def __init__(self):
        self.__ListaViajeros = []
    def AgregarViajero(self,unViajero):
        self.__ListaViajeros.append(unViajero)
    def BuscarV(self,clave):
        for indice,viajero in enumerate(self.__ListaViajeros):
            if (self.__numViajero == clave):
                return indice
    #def buscar(listaobjeto,num):
        #j = 0
        #while j< cont and num !=
            #listaobjeto[j].getnumero():
            #j = j + 1
           #return j

    def testViajero(self):
        pass
