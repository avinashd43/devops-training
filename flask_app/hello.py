from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello(user=None):
  user = user or 'Avinash'
  return render_template('index.html' , myuser=user)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
