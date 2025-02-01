import os
from app import create_app

app = create_app(os.environ.get('FLASK_ENV') or 'default')

SERVER_HOST = os.environ.get('SERVER_HOST') or '0.0.0.0'
SERVER_PORT = os.environ.get('SERVER_PORT') or 4000

if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)