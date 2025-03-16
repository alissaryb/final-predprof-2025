from backend.database import db_session
from backend.services.database_requests import fill_database

db_session.init()
fill_database()
