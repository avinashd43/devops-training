from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST':
    n = request.form['fname']
    a = request.form['fage']

    s = sum(int(d) for d in str(a))
    return render_template('result.html', n=n, s=s)
  else:
    n = request.args['fname']
    a = request.args['fage']

    s = sum(int(d) for d in str(a))
    return jsonify(Name=n, SumofDigits=s)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
