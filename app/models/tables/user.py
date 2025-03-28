from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    nickname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    birth = db.Column(db.Date, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_image = db.Column(db.String)

    def __init__(self, email, nickname, name, birth, password, profile_image=None):
        self.email = email
        self.nickname = nickname
        self.name = name
        self.birth = birth
        self.password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User %r>" % self.name


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','email','nickname','name','birth')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)