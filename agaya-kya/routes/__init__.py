"""Main init file for adding Flask blueprints"""
try:
    from flask import Blueprint
    import os, sys
except ImportError as err:
    raise err

routes = Blueprint("routes", __name__)

# Safe init
@routes.before_request
def set_up_timezone_offset():
    from flask import g

    g.user_timezone_offset = request.headers.get("X-UserTimezoneOffset")


# Main server flask blueprints
from .hello import *
from .megamind import *
from .not_found_handlers import *
