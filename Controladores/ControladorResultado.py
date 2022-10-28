from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorResultado:
    def __init__(self):
        print("Creando ControladorResultado")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()


    def index(self):
        print("Listar todos los Resultados")
        return self.repositorioResultados.findAll()

    """
    Asignacion mesa y candidato a resultado
    """
    def create(self, infoResultado,id_mesa,id_candidato):
        print("Crear un Resultado")
        nuevoResultado = Resultado(infoResultado)
        laMesa= Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        print("Mostrando un Resultado con id ", id)
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificar Resultado (mesa y candidato)
    """
    def update(self, id, infoResultado,id_mesa,id_candidato):
        print("Actualizando Resultado con id ", id)
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_mesa = infoResultado["numero_mesa"]
        resultadoActual.cedula_candidato = infoResultado["cedula_candidato"]
        resultadoActual.numero_votos = infoResultado["numero_votos"]
        laMesa =Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultadoActual.mesa = laMesa
        resultadoActual.candidato = elCandidato
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        print("Eliminando Resultado con id ", id)
        return self.repositorioResultado.delete(id)

    "Obtener todos los resultados de un candidato"

    def listarResultadosDeCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoResultadosDeCandidato(id_candidato)