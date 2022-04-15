from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)

    def __init__(self, user_name):
        self.user_name = user_name

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_name')

user_schema = UserSchema()
multi_user_schema = UserSchema(many=True)


@app.route('/user/add', methods=["POST"])
def add_user():
    post_data = request.get_json()
    user_name = post_data.get('user_name')

    new_user = User(user_name)
    db.session.add(new_user)
    db.session.commit()

    user_schema.dump(new_user)
    return jsonify('new user added.')


@app.route('/login/<user_name>', methods=["GET"])
def login(user_name):
    login = request.form
    
    if user_name == db.login:
        return print('its working')
    else:
        return jsonify('invalid username')

    
    

@app.route('/users/get')
def get_users():
    all_users = db.session.query(User).all()
    return jsonify(multi_user_schema.dump(all_users))



if __name__ == '__main__':
    app.run(debug=True)