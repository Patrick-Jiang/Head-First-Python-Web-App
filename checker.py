from flask import session
from functools import wraps

def check_logged_in(fun):
  @wraps(fun)
  def wrapper(*args,**kwargs):
    if"logged_in" in session:
      return fun(*args,**kwargs)
    return 'You are NOT logged in'
  return wrapper