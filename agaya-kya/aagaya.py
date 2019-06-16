"""Main server file for aagaya-kya"""

__author__ = "Jithin Zacharia"
__version__ = "0.0.1"

try:
    import sys, time, logging
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    from os import urandom
    sys.path.insert(0, "./config")
    from lib.configurationParser import read_configuration
    from routes import *
except ImportError as err:
    raise err
    Flask = None


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(routes)
app.secret_key = read_configuration("SERVER_SECRET")

if __name__ == "__main__":
    if Flask is None:
        logging.critical("Please install Flask framework")
    else:
        logging.warning("--- Starting Flask ---")
        app.run(
            debug=read_configuration("SERVER_DEBUG"),
            port=read_configuration("SERVER_PORT"),
            host=read_configuration("SERVER_HOST"),
        )
