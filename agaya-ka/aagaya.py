'''Main server file for aagaya'''

__author__ = 'Jithin Zacharia'
__version__ = '0.0.1'

try:
    import sys, time, logging
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    from os import urandom
    sys.path.insert(0,'./config')
    from config import server_configuration
    from routes import *
except ImportError as err:
    raise err
    Flask = None


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(routes)
configuration = server_configuration()
app.secret_key = configuration.get_config('SERVER_SECRET')

if __name__ == '__main__':
    if Flask is None:
        logging.critical('Please install Flask framework')
    else:
        logging.warning('--- Starting Flask ---')
        app.run(debug=configuration.get_config('SERVER_DEBUG'),
                port=configuration.get_config('SERVER_PORT'),
                host=configuration.get_config('SERVER_HOST'))



