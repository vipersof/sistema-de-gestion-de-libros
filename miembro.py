class Miembro:
    def __init__(self, dni, nombre):
        self.__dni = dni
        self.__nombre = nombre
        self.__libros_prestados = []   

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getLibrosPrestados(self):
        return self.__libros_prestados

    def agregarLibroPrestado(self, libro):
        self.__libros_prestados.append(libro)

    def quitarLibroPrestado(self, libro):
        self.__libros_prestados.remove(libro)

    def __str__(self):
        if not self.__libros_prestados:
            return (f"Nombre: {self.__nombre} | DNI: {self.__dni} "
                    f"| Libros prestados: ninguno")
        else:
            titulos = ", ".join([l.getTitulo() for l in self.__libros_prestados])
            return (f"Nombre: {self.__nombre} | DNI: {self.__dni} "
                    f"| Libros prestados: {titulos}")
