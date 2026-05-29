from libro import Libro
from miembro import Miembro


# Excepciones personalizadas
class LibroNoEncontradoError(Exception):
    pass

class MiembroNoEncontradoError(Exception):
    pass

class LibroNoDisponibleError(Exception):
    pass

class LibroNoPrestadoError(Exception):
    pass


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__miembros = []

   
    #  AGREGAR   #
    def agregarLibro(self, titulo, autor, isbn):
        """Crea y agrega un libro nuevo. Lanza ValueError si el ISBN ya existe."""
        try:
            self.buscarLibro(isbn)        
            raise ValueError(f"Ya existe un libro con ISBN {isbn}.")
        except LibroNoEncontradoError:
            libro = Libro(titulo, autor, isbn)
            self.__libros.append(libro)
            print(f"✔ Libro '{titulo}' agregado correctamente.")

    def agregarMiembro(self, nombre, dni):
        """Crea y agrega un miembro nuevo. Lanza ValueError si el DNI ya existe."""
        try:
            self.buscarMiembro(dni)
            raise ValueError(f"Ya existe un miembro con DNI {dni}.")
        except MiembroNoEncontradoError:
            miembro = Miembro(dni, nombre)
            self.__miembros.append(miembro)
            print(f"✔ Miembro '{nombre}' agregado correctamente.")

    #  BUSCAR   #
    def buscarLibro(self, isbn):
        """Devuelve el objeto Libro con ese ISBN. Lanza LibroNoEncontradoError si no existe."""
        for libro in self.__libros:
            if str(libro.getIsbn()) == str(isbn):
                return libro
        raise LibroNoEncontradoError(f"No se encontró ningún libro con ISBN {isbn}.")

    def buscarMiembro(self, dni):
        """Devuelve el objeto Miembro con ese DNI. Lanza MiembroNoEncontradoError si no existe."""
        for miembro in self.__miembros:
            if str(miembro.getDni()) == str(dni):
                return miembro
        raise MiembroNoEncontradoError(f"No se encontró ningún miembro con DNI {dni}.")

    #  MOSTRAR  #
    def mostrarLibros(self):
        """Muestra todos los libros registrados."""
        if not self.__libros:
            print("No hay libros registrados.")
            return
        print("\n===== LIBROS =====")
        for libro in self.__libros:
            print(libro)
        print("==================\n")

    def mostrarMiembros(self):
        """Muestra todos los miembros registrados."""
        if not self.__miembros:
            print("No hay miembros registrados.")
            return
        print("\n===== MIEMBROS =====")
        for miembro in self.__miembros:
            print(miembro)
        print("====================\n")


    #  PRÉSTAMO #
  
    def prestarLibro(self, isbn, dni):
        """
        Presta un libro a un miembro.
        Lanza excepciones si el libro o miembro no existen,
        o si el libro ya está prestado.
        """
        try:
            libro = self.buscarLibro(isbn)
            miembro = self.buscarMiembro(dni)

            if libro.getEstado() != "Disponible":
                raise LibroNoDisponibleError(
                    f"El libro '{libro.getTitulo()}' no está disponible. "
                    f"Está prestado a {libro.getMiembroPrestamo().getNombre()}."
                )

            libro.setEstado("Prestado")
            libro.setMiembroPrestamo(miembro)
            miembro.agregarLibroPrestado(libro)

            print(f"✔ Libro '{libro.getTitulo()}' prestado a {miembro.getNombre()} correctamente.")

        except LibroNoEncontradoError as e:
            print(f"Error: {e}")
        except MiembroNoEncontradoError as e:
            print(f"Error: {e}")
        except LibroNoDisponibleError as e:
            print(f"Error: {e}")

    
    #  DEVOLUCIÓN #
    def devolverLibro(self, isbn, dni):
        """
        Registra la devolución de un libro.
        Lanza excepciones si el libro o miembro no existen,
        o si el libro no estaba prestado a ese miembro.
        """
        try:
            libro = self.buscarLibro(isbn)
            miembro = self.buscarMiembro(dni)

            if libro.getEstado() == "Disponible":
                raise LibroNoPrestadoError(
                    f"El libro '{libro.getTitulo()}' ya estaba disponible, no puede devolverse."
                )

            if libro.getMiembroPrestamo().getDni() != miembro.getDni():
                raise LibroNoPrestadoError(
                    f"El libro '{libro.getTitulo()}' no está prestado a {miembro.getNombre()}."
                )

            # Actualizar estado
            libro.setEstado("Disponible")
            libro.setMiembroPrestamo(None)
            miembro.quitarLibroPrestado(libro)

            print(f"✔ Libro '{libro.getTitulo()}' devuelto por {miembro.getNombre()} correctamente.")

        except LibroNoEncontradoError as e:
            print(f"Error: {e}")
        except MiembroNoEncontradoError as e:
            print(f"Error: {e}")
        except LibroNoPrestadoError as e:
            print(f"Error: {e}")

   
    #  CONSULTA DE ESTADO #
   
    def consultarEstadoLibros(self):
        """Muestra el estado de cada libro (disponible o prestado a quién)."""
        if not self.__libros:
            print("No hay libros registrados.")
            return
        print("\n===== ESTADO DE LIBROS =====")
        for libro in self.__libros:
            print(libro)
        print("============================\n")

    def consultarLibrosMiembro(self, dni):
        """Muestra los libros prestados a un miembro específico."""
        try:
            miembro = self.buscarMiembro(dni)
            libros = miembro.getLibrosPrestados()
            print(f"\n===== LIBROS DE {miembro.getNombre().upper()} =====")
            if not libros:
                print("  No tiene libros prestados.")
            else:
                for libro in libros:
                    print(f"  - {libro.getTitulo()} (ISBN: {libro.getIsbn()})")
            print("=" * 35 + "\n")
        except MiembroNoEncontradoError as e:
            print(f"Error: {e}")
