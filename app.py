from flask import Flask, jsonify, abort
from presidents import presidents

app = Flask(__name__)

# FLASK_APP=app.py
# FLASK_ENV=development


@app.route("/", methods=["GET"])
def get_presidents():
    return jsonify(presidents)


@app.route("/<int:president_id>", methods=["GET"])
def get_president(president_id):
    president = next((p for p in presidents if p["id"] == president_id), None)
    if president is None:
        abort(404)
    return jsonify(president)


if __name__ == "__main__":
    app.run(debug=True)
