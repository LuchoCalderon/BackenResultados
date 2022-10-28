from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listar todos los Candidatos")
        self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        print("Crear un Candidato")
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        print("Mostrando un Candidato con id ", id)
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        print("Actualizando Candidato con id ", id)
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        print("Eliminando Candidato con id ", id)
        return self.repositorioCandidato.delete(id)
    """
    Relacion candidato y partido
    """
    def asignarPartido(self,id,id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)




















