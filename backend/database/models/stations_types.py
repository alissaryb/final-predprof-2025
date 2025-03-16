import sqlalchemy
from backend.database.db_session import SqlAlchemyBase


class StationType(SqlAlchemyBase):
    __tablename__ = 'stations_types'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cost = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    radius = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    map_id = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def __repr__(self):
        return f'<StationType> {self.id} {self.type} {self.radius} {self.cost}'
