from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST':
    num1 = int(request.form['integer1'])
    num2 = int(request.form['integer2'])

    sum1 = num1 + num2 
    sub1 = num1 - num2
    mul1 = num1 * num2
    div1 = num1 / num2

    return render_template('result.html', sum1=sum1, sub1=sub1, mul1=mul1, div1=div1)
  else:
    num1 = int(request.args['integer1'])
    num2 = int(request.args['integer2'])

    sum1 = num1 + num2
    sub1 = num1 - num2
    mul1 = num1 * num2
    div1 = num1 / num2

    return jsonify(Sum=sum1, Sub=sub1, Multiply=mul1, Div=div1)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
