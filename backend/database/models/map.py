import sqlalchemy
from backend.database.db_session import SqlAlchemyBase


class Map(SqlAlchemyBase):
    __tablename__ = 'map'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True)
    x = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True)
    y = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    value = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    map_id = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def __repr__(self):
        return f'<Map> {self.id} {self.x} {self.y} {self.value}'
