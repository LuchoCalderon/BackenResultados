from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)

cors = CORS(app)

miControladorMesa = ControladorMesa()
miControladorPartido = ControladorPartido()
miControladorCandidato = ControladorCandidato()
miControladorResultado = ControladorResultado()

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify()

@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def crearResultado(id_mesa,id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data,id_mesa,id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['PUT'])
def modificarResultado(id_resultado,id_mesa,id_candidato):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado,data,id_mesa,id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>",methods = ['DELETE'])
def eliminarResultado(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>",methods=['GET'])
def resultadosDeCandidato(id_candidato):
    json=miControladorResultado.listarResultadosDeCandidato(id_candidato)
    return jsonify(json)

@app.route("/candidatos",methods = ['Post'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/partidos",methods=['Post'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>/partido/<string:id_partido>",methods = ['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json = miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)

@app.route("/mesas",methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("server running : "+ "http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])