from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
  return 'Hello Admin!'

@app.route('/guest/<guest>')
def hello_guest(guest):
  return 'Hello ' + guest + ' as Guest!'

@app.route('/user/<user>')
def hello_user(user):
  if user == 'admin':
    return redirect(url_for('hello_admin'))
  else:
    return redirect(url_for('hello_guest',guest=user))

if __name__ == '__main__':
  app.run('0.0.0.0',debug=True)
