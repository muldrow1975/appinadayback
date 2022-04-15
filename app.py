from flask import Flask, request, render_template
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
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String, Unique=False, nullable=False)
    password = db.Column(db.String, Unique=False, nullable=False)

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_name', 'password')

user_schema = UserSchema()
multi_user_schema = UserSchema()

@app.route('/room1', methods=["GET"])
def Choice_one_page():
    return render_template('choice1.html')


@app.route('/room2', methods=["GET"])
def Choice_two_page():
    return render_template('choice2.html')

@app.route('/room2-1', methods=["GET"])
def Choice_two_one_page():
    return render_template('choice2-1.html')

@app.route('/room2-2', methods=["GET"])
def Choice_two_two_page():
    return render_template('choice2-2.html')


@app.route('/room3', methods=["GET"])
def Choice_three_page():
    return render_template('choice3.html')

@app.route('/room3-1', methods=["GET"])
def Choice_three_one_page():
    return render_template('choice3-1.html')


if __name__ == '__main__':
    app.run(debug=True)