import os
from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
from .model import Object, get_objects, add_object
from datetime import date


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import database
    database.init_app(app)

    @app.route('/')
    def hello():
        return render_template('index.html')


    @app.route('/objects', methods=['GET', 'POST'])
    def objects():
        db = database.get_db()
        cursor = db.cursor()

        if request.method == 'GET':
            query = get_objects.format()
            cursor.execute(query)

            objs = []
            for register in cursor:
                objs.append(Object._make(register))

            database.close_db()
            
            return render_template('objects.html', objs=objs)

        else:
            name = request.form['name']
            description = request.form['description']
            create_date = str(date.today())
            query = add_object.format(name=name, description=description, create_date=create_date)

            cursor.execute(query)
            db.commit()

            database.close_db()

            return redirect(url_for('objects'))

    

    @app.route('/db_test')
    def db_test():
        database.init_db()

        return 'Banco de dados inicializado com sucesso!' 


    return app