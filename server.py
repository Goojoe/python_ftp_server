from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import yaml


def read_yaml(filepath):
    with open(filepath, "rb") as file:
        config = yaml.safe_load(file)
    return config


config = read_yaml("./config.yml")

path = config["path"]
user = config["user"]
password = config["password"]
port = config["port"]

authorizer = DummyAuthorizer()
authorizer.add_user(user, password, path, perm="elradfmwMT")
authorizer.add_anonymous(path, perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", port), handler)
server.serve_forever()
