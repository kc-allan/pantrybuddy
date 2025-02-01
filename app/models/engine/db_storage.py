import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base_model import Base

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')


class DBStorage:
    __session = None
    __engine = None

    def __init__(self):
        """
        Initialize the database connection.
        """
        self.__engine = create_engine(
            f'mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}',
            pool_pre_ping=True,
            pool_recycle=3600,
            echo=True
        )

    def get_session(self):
        """
        Return the session object.
        """
        return self.__session

    def get_engine(self):
        """
        Return the engine object.
        """
        return self.__engine

    def close(self):
        """
        Close the session and the connection to the database.
        """
        self.__session.close()
        self.__engine.dispose()

    def reload(self):
        """
        Create all tables in the database and initialize a new session.
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def commit(self):
        """
        Commit all changes to the database.
        """
        self.__session.commit()

    def rollback(self):
        """
        Rollback all changes to the database.
        """
        self.__session.rollback()

    def delete(self, obj=None):
        """
        Delete an object from the database.
        """
        if obj:
            self.__session.delete(obj)

    def new(self, obj=None):
        """
        Add an object to the database.
        """
        if obj:
            self.__session.add(obj)

    def query_id(self, cls, id):
        """
        Query an object by its id.
        """
        return self.__session.query(cls).get(id)

    def query_all(self, cls):
        """
        Query all objects of a class.
        """
        return self.__session.query(cls).all()

    def query_filter(self, cls, **kwargs):
        """
        Query objects by a filter.
        """
        return self.__session.query(cls).filter_by(**kwargs).all()
