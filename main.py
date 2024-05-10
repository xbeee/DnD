from core import *
import auth

with api.app_context():
    db.create_all()

@api.route('/')
def Index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(api)