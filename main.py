from flask import Flask
from app.routes.users_routes import users


app = Flask(__name__)

app.register_blueprint(users, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)