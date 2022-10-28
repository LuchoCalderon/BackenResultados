from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido
class ControladorPartido:
    def __init__(self):
        print("Creando ControladorPartido")
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listar todos los Partidos")
        return self.repositorioPartido.findAll()

    def create(self,infoPartido):
        print("Crear un Partido")
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)


    def show(self,id):
        print("Mostrando un Partido con id ",id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self,id,infoPartido):
        print("Actualizando Partido con id ",id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        elPartido.nombre = infoPartido["nombre"]
        elPartido.lema = infoPartido["lema"]
        return self.repositorioPartido.save(elPartido)

    def delete(self,id):
        print("Eliminando partido con id ",id)
        return self.repositorioPartido.delete(id)










