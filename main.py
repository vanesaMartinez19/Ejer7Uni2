from ClaseViajeroFrecuentedel7 import ViajeroFrecuente
from ClaseManejadordel7 import Manejador
import csv
def Menu():
    op = 0
    while (op != 4):
        print ("ingrese numero")
        print ("1-Determinar el/los viajero/s con mayor cantidad de millas acumuladas")
        print ("2-Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente.")
        print ("3-anjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente.")
        print ("4-Salir")
        op = int(input(""))
        if (op == 1):
            print("el viajero con mas cantidad de millas tiene: {}".format(ViajeroFrecuente.cantidadTotalM()))
        elif (op == 2):
            i = int(input("ingrese cantidad de millas"))
            ViajeroFrecuente.acumMillas(i)
        elif (op == 3):
            i = int(input("ingrese cantidad de millas a canjear"))
            ViajeroFrecuente.canjeM(i)
def testViajero(true=None):
    archivo = open('ViajerosFrecuentes.csv')
    reader = csv.reader(archivo,delimiter = ',')
    bandera = true
    for fila in reader:
        if bandera:
            bandera = not bandera
        else:
            numViajero = fila[0]
            dni = fila[1]
            Nombre = fila[2]
            Apellido = fila[3]
            millasacum = fila[4]
            Unviajero = ViajeroFrecuente(numViajero,dni,Nombre,Apellido,millasacum)
            self.AgregarViajero(Unviajero)
            archivo.close()

if __name__ == '__main__':
    mb = Manejador()
    mb.testViajero()

    numViajero = int(input("ingrese numero de viajero a buscar"))
    indice = mb.BuscarV(numViajero)
    if indice == None:
        print("numero de viajero: {} Documento: {} Nombre: {} Apellido: {} Millas:{}".format(numViajero ,self.__dni , self.__Nombre , self.__Apellido , self.__millasacum))
        mb.Menu()
