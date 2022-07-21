from flask import Flask, jsonify, request
# Instalo en la terminal mediante el "pip instal ..." el flask, el requests y el jsonify.
# Importo dichas librerías a la API.

import requests

from src.db.db_manager import load_data_restrictions, save_dietary_restriction
# Importo las funciones que provienen del data base maganer:
#       - La función save_id_param me permite almacenar lo que se ingresa mediante el método HHTP POST.
#       - La función load_data_restrictions me permite mostrar la información del archivo csv.

from src.models.flights import Flights

app = Flask(__name__)
# El constructor me permite crear una instancia de un objeto especial y  guardarlo en la variable "app".

data_restrictions = load_data_restrictions()
# Guardo la información de la función load_data en la variable "data". Esta variable devuelve una lista de objetos.
data_flights = []
# Guardo la data de los flights.


# 1) [GET]: Obtener el listado de diatery restrictions provenientes del archivo csv.
@app.route(r'/api/dietary_restrictions', methods=['GET'])
def get_restrictions():
    return jsonify([dietary_restric.serialize() for dietary_restric in data_restrictions])


# 2) [GET]
@app.route(r'/api/dream-on/flights/<user_id>', methods=['GET'])
def get_flights(user_id):

    user_id_param = request.args.get('flight_id', '')
    # Si no encuentra flight_id devuelve un error.

    http_rsp_user = requests.get(
        "https://ucema-fdi-recuperatorio.herokuapp.com/api/dream-on/flights?user_id=" + str(user_id),
        )
    print(user_id)
    print(http_rsp_user)
    # Ambos print los estoy usando para encontrar en que línea me esta tirando el error.
    status_code = http_rsp_user.status_code
    if status_code == 200:
        json = http_rsp_user.json()
        flights = []
        return jsonify(json)

    else:

        return jsonify(
            error_code="ERROR_BAD",
            error_description="Not found",
            error_body=''
        ), 404



# 3) [POST]: Ingreso desde el Postman data que con la función save_id_param la guardo en un csv
@app.route(r'/api/dream-on/flights', methods=['POST'])
def create_stat():
    user_id_param = request.args.get("user_id", "")

    if user_id_param == "client_test_21":
        req_json = request.json
        try:
            save_dietary_restriction(req_json)

        except KeyError as key_err:
            missing_param = (key_err.__str__())
            return jsonify(
                error_code=400,
                error_description="Bad request",
                error_body=missing_param
            ), 400

    return jsonify({'data_dietary': req_json})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # Defino el número del puerto al que voy a ir a buscar la información de la API en el Postman.
