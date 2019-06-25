from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost:5432/blog_api_db'
db = SQLAlchemy(app)

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    blogposts = db.relationship('BlogpostModel', backref='users', lazy=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    class BlogpostModel(db.Model):
        __tablename__ = 'blogposts'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(128), nullable=False)
        contents = db.Column(db.Text, nullable=False)
        owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        created_at = db.Column(db.DateTime)
        modified_at = db.Column(db.DateTime)

        def __init__(self, data):
            self.title = data.get('title')
            self.contents = data.get('contents')
            self.created_at = datetime.datetime.utcnow()
            self.modified_at = datetime.datetime.utcnow()
            self.owner_id = data.get('owner_id')
            self.created_at = datetime.datetime.utcnow()
            self.modified_at = datetime.datetime.utcnow()

    def __repr(self):
        return '<id {}>'.format(self.id)

db.create_all()