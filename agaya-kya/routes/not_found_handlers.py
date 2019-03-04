'''Main error handlers for flask'''
try:
    import os, sys
    from flask import request, jsonify
    from . import routes
except ImportError as err:
    raise err

@routes.app_errorhandler(404)
def not_found(e):
    return jsonify('The route you requested is not found')

@routes.app_errorhandler(500)
def internal_server_error(e):
    return jsonify('Internal error occured, Please try again later')

@routes.app_errorhandler(403)
def forbidden_error(e):
    return jsonify('Forbidden!!! Error occured, Try again later')