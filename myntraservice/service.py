from flask import Flask
from flask_restful import Resource, Api
from handler.ping import Ping
from handler.user import User

from flask import request 


app = Flask(__name__)
api = Api(app)
api.add_resource(Ping, '/ping/')
api.add_resource(User, '/user/')





if __name__ == '__main__':
    app.run(debug=True)