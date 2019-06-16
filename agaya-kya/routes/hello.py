try:
    import os, sys
    from flask import request, jsonify
    from . import routes
except ImportError as err:
    raise err


@routes.route("/ping")
def ping():
    return jsonify("Agaya is alive")
