from biblioteca import Biblioteca


def mostrarMenu():
    print("\n========== BIBLIOTECA ==========")
    print("1 - Agregar libro")
    print("2 - Agregar miembro")
    print("3 - Mostrar todos los libros")
    print("4 - Mostrar todos los miembros")
    print("5 - Prestar libro")
    print("6 - Devolver libro")
    print("7 - Consultar estado de libros")
    print("8 - Consultar libros de un miembro")
    print("0 - Salir")
    print("================================\n")


def main():
    biblioteca = Biblioteca()

    while True:
        mostrarMenu()

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "0":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            elif opcion == "1":
                titulo = input("Título del libro: ").strip()
                autor  = input("Autor del libro: ").strip()
                isbn   = input("ISBN del libro: ").strip()
                biblioteca.agregarLibro(titulo, autor, isbn)

            elif opcion == "2":
                nombre = input("Nombre del miembro: ").strip()
                dni    = input("DNI del miembro: ").strip()
                biblioteca.agregarMiembro(nombre, dni)

            elif opcion == "3":
                biblioteca.mostrarLibros()

            elif opcion == "4":
                biblioteca.mostrarMiembros()

            elif opcion == "5":
                isbn = input("ISBN del libro a prestar: ").strip()
                dni  = input("DNI del miembro: ").strip()
                biblioteca.prestarLibro(isbn, dni)

            elif opcion == "6":
                isbn = input("ISBN del libro a devolver: ").strip()
                dni  = input("DNI del miembro que devuelve: ").strip()
                biblioteca.devolverLibro(isbn, dni)

            elif opcion == "7":
                biblioteca.consultarEstadoLibros()

            elif opcion == "8":
                dni = input("DNI del miembro: ").strip()
                biblioteca.consultarLibrosMiembro(dni)

            else:
                print("Opción inválida. Ingresá un número del 0 al 8.")

        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
