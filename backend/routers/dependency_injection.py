from functools import wraps
from backend.database import db_session


def inject_session():
    def decorator(route_func):
        @wraps(route_func)
        def wrapper(*args, **kwargs):
            session = db_session.create_session()
            res = route_func(session, *args, **kwargs)
            session.close()
            return res
        return wrapper
    return decorator
