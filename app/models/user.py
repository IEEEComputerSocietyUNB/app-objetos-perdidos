from sqlalchemy import Column, Integer, String, DateTime, func
from .base import Base

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(20))
    password = Column(String(80), nullable=False)
    create_date = Column(DateTime, default=func.now())

    def __repr__(self):
        return f'User {self.name}'

    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.passowrd,
            'create_date': self.create_date
        }
