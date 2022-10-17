from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_json import FlaskJSON

app = Flask(__name__)
api = Api(app)
CORS(app)
FlaskJSON(app)

class employeetoAnalyze(Resource):
    def post(self):
        response = request.get_json()
        name = response['nombre']
        photo = response['foto']


api.add_resource(employeetoAnalyze, '/emp')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')