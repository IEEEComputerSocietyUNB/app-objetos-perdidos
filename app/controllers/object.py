from ..models.object import Object
from ..db import db_session
from werkzeug.utils import secure_filename
from flask import flash, redirect
import os

UPLOAD_FOLDER='/var/www/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class ObjectController():
    @staticmethod
    def get_objects():
        session = db_session()

        objects = session.query(Object).all()

        session.close()

        return objects


    @staticmethod
    def get_object(id):
        session = db_session()

        obj = session.query(Object).filter_by(id=id).first()

        session.close()

        return obj


    @staticmethod
    def create(request):
        name = ''
        description = ''
        reward = ''
        image_path = ''

        if request.is_json:
            content = request.get_json()
            name = content['name']
            description = content['description']
            reward = content['reward']
        else:
            name = request.form['name']
            description = request.form['description']
            reward = request.form['reward']

        if 'object_image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        else:
            file = request.files['object_image']

            if file.filename == '':
                image_path = '#'

            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                image_path = filename

        obj = Object(name=name, description=description, reward=reward, image_path=image_path)

        session = db_session()

        result = ''
        try: 
            session.add(obj)
        except:
            session.rollback()
            result = 'failure'
        else:
            session.commit()
            result = 'success'

        if request.is_json:
            result = obj.serialize()

        session.close()

        return result


    @staticmethod
    def update(id, request):
        name = ''
        description = ''
        reward = ''
        image_path = ''

        if request.is_json:
            content = request.get_json()
            name = content['name']
            description = content['description']
            reward = content['reward']
            image_path = content['image_path']
        else:
            name = request.form['name']
            description = request.form['description']
            reward = request.form['reward']
            image_path = '#'

        session = db_session()

        result = ''
        try: 
            obj = session.query(Object).filter_by(id=id).update(
                {
                    'name': name,
                    'description': description,
                    'reward': reward,
                    'image_path': image_path,
                }, synchronize_session='fetch')

        except:
            session.rollback()
            result = 'failure'
        else:
            session.commit()
            result = 'success'

        if request.is_json:
            obj = session.query(Object).filter_by(id=id).first()
            result = obj.serialize()

        session.close()

        return result


    @staticmethod
    def delete(id):
        session = db_session()

        result = ''
        try:
            obj = session.query(Object).filter_by(id=id).delete(
                synchronize_session='fetch')
        except:
            session.rollback()
            result = 'failure'
        else:
            session.commit()
            result = 'success'

        session.close()

        return result
    


    @staticmethod
    def fill_table():
        obj1 = Object(name='Mi Band 3', description='Relógio pulseira preta', reward='Um muito obrigado!', image_path='#')
        obj2 = Object(name='Rolex', description='Relógio suiço de R$ 20.000', reward='', image_path='#')

        session = db_session()

        result = ''
        try: 
            session.add(obj1)
            session.add(obj2)
        except:
            session.rollback()
            result = 'failure'
        else:
            session.commit()
            result = 'success'

        session.close()

        return result
