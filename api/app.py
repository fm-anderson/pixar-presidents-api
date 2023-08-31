from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from api.presidents import presidents

app = Flask(__name__)
CORS(
    app,
    origins=[
        "https://presidents.fm-anderson.com/",
        "https://presidents-memory.netlify.app/",
    ],
)

limiter = Limiter(app, key_func=get_remote_address)
logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=["GET"])
@limiter.limit("20 per minute")
def get_presidents():
    return jsonify(presidents)


@app.route("/<int:president_id>", methods=["GET"])
@limiter.limit("20 per minute")
def get_president(president_id):
    president = next((p for p in presidents if p["id"] == president_id), None)
    if president is None:
        abort(404)
    return jsonify(president)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    app.run(debug=True)


# FLASK_APP=app.py
# FLASK_ENV=development
