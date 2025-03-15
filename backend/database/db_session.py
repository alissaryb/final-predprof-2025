import os

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

from dotenv import load_dotenv


SqlAlchemyBase = dec.declarative_base()

session_factory = None


def init():
    global session_factory

    if session_factory:
        return

    load_dotenv()

    conn_str = os.getenv("DATABASE_URL")
    if not conn_str:
        conn_str = 'sqlite:///backend/database/predprof.db?check_same_thread=False'
    print('Connecting to database...')

    engine = sa.create_engine(conn_str, echo=False, pool_timeout=60, pool_size=100, max_overflow=200)
    session_factory = orm.sessionmaker(bind=engine, expire_on_commit=False)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global session_factory
    return session_factory()
