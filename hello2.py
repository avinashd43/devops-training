from flask import Flask

app = Flask(__name__)

@app.route('/<var>')
def hello(var):
  return 'Hello '  + var + '!'

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
