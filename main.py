from core import *
import auth

with api.app_context():
    db.create_all()

if __name__ == '__main__':
    socketio.run(api)