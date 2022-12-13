from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST':
    n = float(request.form['fnum'])
    a = float(request.form['snum'])

    return render_template('result.html', s=n+a, d=n-a, d1=n/a, m=n*a)
  else:
    n = float(request.args['fnum'])
    a = float(request.args['snum'])

    return jsonify(Sum=n+a, Difference=n-a, Division=n/a, Multiplication=n*a)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

