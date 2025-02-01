from app.models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()

# Import the models here
from app.models.user import User as User
