from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<var>')
def hello(var=None):
  if var is None:
    return 'Hello Avinash!'
  else:
    return 'Hello '  + var

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
