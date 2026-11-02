from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="erreur")


@app.get("/version")
def version():
    return jsonify(version="1.0.0")


@app.get("/tickets")
def tickets():
    return jsonify([
        {"id": 1, "titre": "Probleme de connexion Wi-Fi", "statut": "ouvert"},
        {"id": 2, "titre": "Imprimante indisponible", "statut": "resolu"}
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)