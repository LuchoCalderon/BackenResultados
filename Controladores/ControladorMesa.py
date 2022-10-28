from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorMesa:
    def __init__(self):
        print("Creando ControladorMesa")
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        print("Listar todas las Mesas")
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        print("Crear una Mesa")
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        print("Mostrando una Mesa con id ", id)
        lamesa = Mesa(self.repositorioMesa.findById(id))
        return lamesa.__dict__

    def update(self, id, infoMesa):
        print("Actualizando Mesa con id ", id)
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        print("Eliminando Mesa con id ", id)
        return self.repositorioMesa.delete(id)