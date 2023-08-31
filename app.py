from flask import Flask, jsonify, abort
from flask_cors import CORS
from presidents import presidents

app = Flask(__name__)
CORS(
    app,
    origins=[
        "https://presidents.fm-anderson.com/",
        "https://presidents-memory.netlify.app/",
    ],
)


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


# FLASK_APP=app.py
# FLASK_ENV=development
