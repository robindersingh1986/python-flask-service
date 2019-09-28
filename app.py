from flask import Flask, request
app = Flask(__name__)



from routes.admin.index import admin
from routes.user.index import user

@app.route('/know')
def knowserver():
  return {
    'REMOTE_ADDR' : request.environ.get('REMOTE_ADDR'),
    'HTTP_ORIGIN' : request.environ.get('HTTP_ORIGIN'),
    'HTTP_X_FORWARDED_HOST' : request.environ.get('HTTP_X_FORWARDED_HOST'),
    'HTTP_REFERER' : request.environ.get('HTTP_REFERER')
  }

@app.route('/shutdown')
def shutdown():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  else:
    try:
      func()
      return 'Shutting down gracefully...'
    except:
      return "error encountered"



app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user)

#export FLASK_APP=flaskr
