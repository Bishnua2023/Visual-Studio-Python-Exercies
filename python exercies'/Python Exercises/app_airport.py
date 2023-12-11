# app_airport.py

from flask import Flask, jsonify

app = Flask(__name__)

# airport database (ICAO code as key)
airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    # more airports to be added or connected to airport database
}

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport_info = airport_database.get(icao_code)
    if airport_info:
        response = {"ICAO": icao_code, "Name": airport_info["Name"], "Location": airport_info["Location"]}
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404
