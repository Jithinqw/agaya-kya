'''Flask route for Flask route'''
try:
    import os, sys
    from flask import request, jsonify
    from . import routes
    from lib import book_my_show_parser
except ImportError as err:
    raise err

@routes.route('/getdetailsbycity', methods=['POST'])
def getdetailsbycity():
    try:
        city = request.json['city']
        parser = book_my_show_parser.parser()
        print(parser.get_html(city))
        return jsonify(parser.get_now_showing(parser.get_html(city)))
    except Exception as err:
        return "%s"%err
    
@routes.route('/getdetailsbymovie', methods=['POST'])
def getdetailsbymovie():
    return jsonify('Movie')
