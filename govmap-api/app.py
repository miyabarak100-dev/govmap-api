from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route("/address")
def address():
    gush = request.args.get("gush")
    helka = request.args.get("helka")

    if not gush or not helka:
        return jsonify({"error": "Missing gush or helka"}), 400

    url = f"https://es.govmap.gov.il/TldSearch/api/BlockParcelSearch?block={gush}&parcel={helka}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        address = data.get("fullAddress") or data.get("address")

    except:
        address = None

    return jsonify({
        "gush": gush,
        "helka": helka,
        "address": address
    })



