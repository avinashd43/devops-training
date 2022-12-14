from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
import pyodbc
import jsonpickle

server = 'remotemysql.com'
database = 'vsF4Cfo0Ne'
username = 'vsF4Cfo0Ne'
password = 'Qkk0UXYn7W'
mystring='DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
cnxn = pyodbc.connect(mystring)
cursor = cnxn.cursor()

query = "CREATE TABLE IF NOT EXISTS AVINASH_STATS (Request varchar(6) NOT NULL,num1 FLOAT NOT NULL,num2 FLOAT NOT NULL, sum1 FLOAT NOT NULL, sub1 FLOAT NOT NULL, mul1 FLOAT NOT NULL, div1 FLOAT NOT NULL);"
#query = "DROP TABLE AVINASH_STATS;"

cursor.execute(query)
cursor.commit()
def exec(query, method, num1, num2, sum1, sub1, mul1, div1):
  cursor.execute(query,(method, num1, num2, sum1, sub1, mul1, div1)) 
  cursor.commit()
  
def printdata():
  query = "SELECT * FROM AVINASH_STATS"
  d = cursor.execute(query)
  row = d.fetchall()
  return row

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST':
    num1 = int(request.form['integer1'])
    num2 = int(request.form['integer2'])
    method = "'" + request.method + "'" 
    sum1 = num1 + num2 
    sub1 = num1 - num2
    mul1 = num1 * num2
    div1 = num1 / num2
    query = '''INSERT INTO AVINASH_STATS (Request, num1, num2, sum1, sub1, mul1, div1) VALUES(?, ?, ?, ?, ?, ?, ? );
'''
    exec(query,method, num1, num2, sum1, sub1, mul1, div1)
    #printdata()
    return render_template('result.html', sum1=sum1, sub1=sub1, mul1=mul1, div1=div1)
  else:
    num1 = int(request.args['integer1'])
    num2 = int(request.args['integer2'])
    method = "'" + request.method + "'" 
    sum1 = num1 + num2
    sub1 = num1 - num2
    mul1 = num1 * num2
    div1 = num1 / num2
    query = '''INSERT INTO AVINASH_STATS (Request, num1, num2, sum1, sub1, mul1, div1) VALUES(?, ?, ?, ?, ?, ?, ? );
'''
    exec(query,method, num1, num2, sum1, sub1, mul1, div1)
    #printdata()

    return jsonify(Sum=sum1, Sub=sub1, Multiply=mul1, Div=div1)
@app.route('/printdata')
def printda():
  d = printdata()
  return render_template('audit.html', d=d)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
