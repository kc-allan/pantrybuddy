from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


from uuid import uuid4
from datetime import datetime

Base = declarative_base()

fmt_time = '%Y-%m-%d %H:%M:%S'


class BaseModel:
    id = Column(String(64), primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().strftime(fmt_time)
        self.updated_at = self.created_at
        from app.models import storage
        storage.new(self)

    def save(self):
        from app.models import storage
        self.updated_at = datetime.now().strftime(fmt_time)
        storage.commit()

    def delete(self):
        from app.models import storage
        storage.delete(self)
        self.save()

    def serialize(self):
        return self.to_dict()

    def to_dict(self):
        model_dict = self.__dict__.copy()
        model_dict['created_at'] = model_dict['created_at'].strftime(fmt_time)
        model_dict['updated_at'] = model_dict['updated_at'].strftime(fmt_time)
        for key in model_dict.keys():
            # Remove private and protected attributes
            if key.startswith('_'):
                model_dict.pop(key, None)
        return model_dict
