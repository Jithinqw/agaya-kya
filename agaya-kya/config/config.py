"""Main class for loading server configuration"""


class server_configuration:
    def __init__(self):
        self.app_name = "aagaya-ka"
        self.app_config = {
            "SERVER_PORT": 5000,
            "SERVER_DEBUG": True,
            "SERVER_HOST": "localhost",
            "SERVER_SECRET": "winter is coming",
            "IS_UNDER_MAINTAINCE": False,
        }

    def get_config(self, key):
        if key is None:
            return False
        else:
            return self.app_config[key]
