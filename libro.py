class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__estado = "Disponible"   
        self.__miembro_prestamo = None 

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getIsbn(self):
        return self.__isbn

    def getEstado(self):
        return self.__estado

    def getMiembroPrestamo(self):
        return self.__miembro_prestamo

    def setEstado(self, estado):
        self.__estado = estado

    def setMiembroPrestamo(self, miembro):
        self.__miembro_prestamo = miembro
 
    def __str__(self):
        if self.__estado == "Disponible":
            return (f"Título: {self.__titulo} | Autor: {self.__autor} "
                    f"| ISBN: {self.__isbn} | Estado: {self.__estado}")
        else:
            return (f"Título: {self.__titulo} | Autor: {self.__autor} "
                    f"| ISBN: {self.__isbn} | Estado: {self.__estado} "
                    f"| Prestado a: {self.__miembro_prestamo.getNombre()}")
