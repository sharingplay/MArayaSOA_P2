from tkinter import image_names
import pymysql.cursors
from flask import Flask, render_template, request, jsonify
from flask_json import FlaskJSON, json_response
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_restful_swagger_2 import Api
from sqlalchemy import text
from flaskext.mysql import MySQL
import os
import json
import google.auth
import vision

import re

app = Flask(__name__)
api = Api(app)
CORS(app)
FlaskJSON(app)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "password"
app.config["MYSQL_DATABASE_DB"] = "imageAnalysis"
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = 3306
mysql.init_app(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    return json_response(data_=data, headers_=headers, status_=code)


class Images(Resource):
    def get(self):
        try:
            '''
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("select * from images;")
            data = cursor.fetchall()
            resp = jsonify(data)
            '''

            f = open('images.json')
            data = json.load(f)

            bytes = re.search(",.*", data["images"][1]["image"]).group().replace(",", "")
            print(bytes)


            vision.analyze_emotion(data["images"][1]["image"])

            return data
        except Exception as e:
            print(e)

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            #print(test)
            cursor.execute("insert into images(imageName,dateAdded,image) values ('Mario', '2021-07-10 22:11:24', 'texto prueba');")
            #cursor.execute("select * from images;")
            data = cursor.fetchall()
            resp = jsonify(data)
            resp.status_code = 200
            return 
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


class status(Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


api.add_resource(Images, '/Images')
api.add_resource(status, '/')
credentials, project = google.auth.default()


if __name__ == '__main__':


    app.run()