from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .user import User

class Object(Base):
    __tablename__ = 'Objetcs'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500))
    create_date = Column(DateTime, default=func.now())
    reward = Column(String(200))
    image_path = Column(String(100))
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship(User)    

    def __repr__(self):
        return f'Object {self.name}'

    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'create_date': self.create_date,
            'reward': self.reward,
            'image_path': self.image_path,
            'user_id': self.user_id
        }
