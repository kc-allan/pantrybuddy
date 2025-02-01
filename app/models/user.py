from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base_model import Base, BaseModel

PERMISSIONS = {
    'create': 1,
    'read': 2,
    'update': 4,
    'delete': 8
}

ROLES = {
    'admin': PERMISSIONS['create'] | PERMISSIONS['read'] | PERMISSIONS['update'] | PERMISSIONS['delete'],
    'user': PERMISSIONS['read']
}


class User(BaseModel, Base): # type: ignore
    __tablename__ = 'users'

    username = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    fullname = Column(String(64), nullable=False)
    _password = Column(String(128), nullable=False)
    role = Column(String(64), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', password='{self.password}')>"
