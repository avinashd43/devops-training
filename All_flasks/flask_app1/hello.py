from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  n = request.form['fname']
  a = request.form['fage']

  s = sum(int(d) for d in str(a))
  return render_template('result.html', n=n, s=s)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
