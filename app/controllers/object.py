from ..models.object import Object
from ..db import db_session

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
            image_path = content['image_path']
        else:
            name = request.form['name']
            description = request.form['description']
            reward = request.form['reward']
            image_path = '#'

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
