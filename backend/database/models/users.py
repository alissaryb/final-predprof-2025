import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from backend.database.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)  # UUID
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        return f'<User> {self.id} {self.email} {self.name}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password, method='pbkdf2:sha256:1000')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
