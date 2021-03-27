from flask import Flask, render_template, url_for, request, redirect
from .db import init_db
from .models.object import Object
from .controllers.object import ObjectController
from flask import jsonify


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import database
    database.init_app(app)


    @app.route('/')
    def hello():
        init_db() 

        ObjectController.fill_table()

        return redirect(url_for('view_objects'))


    @app.route('/objects/create', methods=['GET', 'POST'])
    def create_object():
        if request.method == 'GET':
            return render_template('registerObject/index.html')

        else:
            ObjectController.create(request)

            return redirect(url_for('view_objects'))


    @app.route('/objects/view', methods=['GET'])
    def view_objects():
        objs = ObjectController.get_objects()
        
        return render_template('showCase/index.html', objs=objs)


    @app.route('/login', methods=['GET', 'POST'])
    def login():

        return render_template('login/index.html')


    @app.route('/signup', methods=['GET', 'POST'])
    def signup():

        return render_template('signUp/index.html')
        

    @app.route('/objects', methods=['GET', 'POST'])
    def json_objects_get_or_create():
        if request.method == 'POST':
            return ObjectController.create(request)

        objs = ObjectController.get_objects()
        return jsonify(eqtls=[obj.serialize() for obj in objs])


    @app.route('/objects/<int:id>', methods=['PUT', 'DELETE'])
    def json_object_get_or_update_or_delete(id):
        if request.method == 'DELETE':
            result = ObjectController.delete(id)

            return jsonify(status='success')
        
        else:
            return ObjectController.update(id, request)
    

    @app.route('/db_test')
    def db_test():
        database.init_db()

        return 'Banco de dados inicializado com sucesso!' 


    return app