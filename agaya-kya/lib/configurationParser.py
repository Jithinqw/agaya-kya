import os
import configparser
from exceptions.serverExceptions import KeyNotProvidedError, ResourceNotFound


def read_configuration(key):
    config = configparser.ConfigParser()
    default_folder = os.path.dirname(os.path.abspath(__file__))
    file_folder = os.path.join(default_folder, "config.ini")
    config.read(file_folder)
    if not key:
        raise KeyNotProvidedError("Key is not provided")
    if config.get("server", key) is None:
        raise ResourceNotFound("Resource for the key is not found")
    else:
        return config.get("server", key)
