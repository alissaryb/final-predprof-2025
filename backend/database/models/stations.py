import sqlalchemy
from backend.database.db_session import SqlAlchemyBase


class Station(SqlAlchemyBase):
    __tablename__ = 'stations'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    x = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True)
    y = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cost = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    radius = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    map_id = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def __repr__(self):
        return f'<Station> {self.id} {self.x} {self.y} {self.type}'
