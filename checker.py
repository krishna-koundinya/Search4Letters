from flask import session

from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper():
        if 'logged_in' in session:
            return func()
        return 'You are not logged in.'
    return wrapper
