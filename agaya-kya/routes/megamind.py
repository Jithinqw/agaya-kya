"""Flask route for Flask route"""
try:
    import os, sys
    from flask import request, jsonify
    from . import routes
    from lib import book_my_show_parser
except ImportError as err:
    raise err


@routes.route("/getdetailsbycity", methods=["POST"])
def getdetailsbycity():
    try:
        city = request.json["city"]
        parser = book_my_show_parser.parser()
        if len(parser.get_now_showing(parser.get_html(city))) is 0:
            return jsonify(
               "No user films found for this city or this city does not exist"
            )
        else:
            return jsonify(parser.get_now_showing(parser.get_html(city)))
    except Exception as err:
        return "%s" % err
