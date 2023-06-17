
from Revista import Revista
from Libro import Libro
from datetime import date


class Pedido:
    contador_pedido = 0

    def __init__(self, solicitante: str, lista_material: list, materia: str):
        self._id = Pedido.contador_pedido + 1
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._materia = materia
        self._fecha_prestamo = date.today()
        self._fecha_devolucion = None
        Pedido.contador_pedido += 1

    @property
    def id(self):
        return self._id

    @property
    def solicitante(self):
        return self._solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @property
    def materia(self):
        return self._materia

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    def pedir_material(self, material):
        self._lista_material.append(material)

    def devolver_material(self, material):
        if material in self._lista_material:
            self._lista_material.remove(material)
        else:
            print("El material no se encuentra en la lista de préstamo.")

    def completar_prestamo(self):
        self._fecha_devolucion = date.today()


if __name__ == "__main__":
    libro1 = Libro("12345", "Jame Yepez", "Libro CULPABLES", 2023, "Editorial 345", True, 10, "Tapa dura")
    libro2 = Libro("67890", "Dome Anchundia", "Libro ORGULLO Y PREJUICIO", 2022, "Editorial 890J8", False, 5,
                   "Tapa blanda")
    revista1 = Revista("09456", "Jame Yepez", "Revista Espejo", 2023, "Editorial 908", True, 10, "Moda")
    revista2 = Revista("67890", "Dome Anchundia", "Revista Tecnology", 2022, "Editorial 876", False, 5, "Tecnología")
    revista3 = Revista("36533", "Livintong Gallardo", "Revista De Inteligencia Artificial", 2021, "Editorial 430", False, 8,
                       "Inteligencia Artificial")
    pedido1 = Pedido("Estudiante 1", [libro1, revista1], "Matemáticas")
    pedido2 = Pedido("Docente 1", [libro2, revista2, revista3], "Informática")

    print("Datos del Pedido 1:")
    print("ID:", pedido1.id)
    print("Solicitante:", pedido1.solicitante)
    print("Materia:", pedido1.materia)
    print("Fecha de Préstamo:", pedido1.fecha_prestamo)
    print("Fecha de Devolución:", pedido1.fecha_devolucion)
    print("Lista de Materiales:")
    for material in pedido1.lista_material:
        print(material.titulo)
    print()

    print("Datos del Pedido 2:")
    print("ID:", pedido2.id)
    print("Solicitante:", pedido2.solicitante)
    print("Materia:", pedido2.materia)
    print("Fecha de Préstamo:", pedido2.fecha_prestamo)
    print("Fecha de Devolución:", pedido2.fecha_devolucion)
    print("Lista de Materiales:")
    for material in pedido2.lista_material:
        print(material.titulo)
    print()

    pedido1.pedir_material(libro2)
    pedido2.devolver_material(revista2)

    print("Lista de Materiales después de modificar:")
    for material in pedido1.lista_material:
        print(material.titulo)
    print()

    pedido1.completar_prestamo()
    pedido2.completar_prestamo()

    print("Fecha de Devolución actualizada:")
    print("Pedido 1:", pedido1.fecha_devolucion)
    print("Pedido 2:", pedido2.fecha_devolucion)
