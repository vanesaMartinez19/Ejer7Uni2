class ViajeroFrecuente:
    __numViajero = 0
    __dni = ''
    __Nombre = ''
    __Apellido=''
    __millasacum = 0
    def __init__(self, numViajero, dni, Nombre, Apellido, millasacum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__millasacum = millasacum
    def __getNumViajero(self):
        return self.__numViajero
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__Nombre
    def getApellido(self):
        return self.__Apellido
    def getMillasAcum(self):
        return self.__millasacum


    def mostrarDatos(self):
        return ('Numero de viajero :{}, Apellido : {}, Nombre: {} , Dni: {} , Millas acumluladas: {} '.format(self.__numViajero, self.__Apellido, self.__Nombre, self.__dni, self.__millasacum))
    def cantidadTotalM(self,Lista):
        for i,viajero in enumerate(self.__ListaViajeros):
            if ( '1000000' == Lista[i].__getMillasAcum):
                j = i
        return print("El pasajero con mas millas acumuladas es {} {} con millas {}".format(Lista[j].__Nombre, Lista[j].__Apellido, Lista[j].__millasacum))

    def acumMillas(self,millas):
        self.__millasacum = +millas
        return self.__millasacum
    def canjeM(self,millas):
        if self.__millasacum>=millas:
                self.__millasacum = +millas
                #return self.__millasacum
                return print("La cantidad de millas acumuladas son {}".format(self.__millasacum))
        else:
            return print("error")
