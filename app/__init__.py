import os
from flask import Flask, render_template, url_for
import mysql.connector


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return render_template('index.html')
    
    @app.route('/db_test')
    def db():
        db = mysql.connector.connect(
            host="localhost", 
            user="dev", 
            password="password"
        )

        cursor = db.cursor()

        result = cursor.execute("SHOW DATABASES")

        result = ""
        for register in cursor:
            result += str(register)

        return str(result)



    return app