from flask import Flask
from flask_restful import Resource, Api
from handler import Ping

from flask import request 


app = Flask(__name__)
api = Api(app)


api.add_resource(Ping, '/ping/')





if __name__ == '__main__':
    app.run(debug=True)