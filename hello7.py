from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello(user=None):
  user = user or 'Sagar'
  return'''
    <html>
    <head>
      <title>Welcome to Flask</title>
    </head>
    <body>
      <h1>Welcome %s !</h1>
    </body>
    </html>''' % user

if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
