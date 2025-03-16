import sqlalchemy
from backend.database.db_session import SqlAlchemyBase


class Module(SqlAlchemyBase):
    __tablename__ = 'modules'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True)
    x = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    y = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    map_id = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def __repr__(self):
        return f'<Module> {self.id} {self.x} {self.y} {self.type}'
