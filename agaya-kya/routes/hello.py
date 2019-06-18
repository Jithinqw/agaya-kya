try:
    from flask import jsonify
    from . import routes
except ImportError as err:
    raise err


@routes.route("/ping")
def ping():
    return jsonify("Agaya is alive")
