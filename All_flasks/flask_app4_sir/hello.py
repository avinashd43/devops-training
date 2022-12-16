AKCp8nyY8nL6hiSNZkCr2kSG1YSdQqYcL2U8M9aRsMQ9oHaXDHCAfQV3pgi5synQUfTBi76qG

sudo mkdir -p /var/www/hello ; sudo cp -fr * /var/www/hello/ ; sudo chmod -R 775 /var/
www/hello ; sudo cp -fr /var/www/hello/hello.service /etc/systemd/system/ ; sudo systemctl
daemon-reload ; sudo systemctl start hello

from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

def conn():
  server = 'remotemysql.com'
  database = 'vsF4Cfo0Ne'
  username = 'vsF4Cfo0Ne'
  password = 'Qkk0UXYn7W'
  mystring='DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=' server ';DATABASE=' database ';UID=' username ';PWD=' password

  cnxn = pyodbc.connect(mystring)
  cursor = cnxn.cursor()
  return cursor

def exec(query):
  c = conn()
  c.execute(query)
  c.commit()
  return c


def createtableifnot():
  query = "CREATE TABLE IF NOT EXISTS SAGAR_STATS (method varchar(6) NOT NULL,fnum FLOAT NOT NULL,snum FLOAT NOT NULL, sum FLOAT NOT NULL, difference FLOAT NOT NULL, multiply FLOAT NOT NULL, division FLOAT NOT NULL);"
  c = exec(query)
  c.close()

def insert(method,fnum,snum,s,d,d1,m):
  query = "INSERT INTO SAGAR_STATS VALUES('"   method   "', "   str(fnum)   ", "   str(snum)   ", "   str(s)   ", "   str(d)   ", "   str(d1)   ", "   str(m)   ");"
  c = exec(query)
  c.close()

#INSERT INTO SAGAR_STATS VALUES('GET', 10, 20, 30, -10, 0.5, 200);

def printdata():
  query = "SELECT * from SAGAR_STATS;"
  c = exec(query)
  d = c.fetchall()
  c.close()
  return d


@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST':
    n = float(request.form['fnum'])
    a = float(request.form['snum'])
    createtableifnot()
    insert(request.method, n, a, n a, n-a, n/a, n*a)

    return render_template('result.html', s=n a, d=n-a, d1=n/a, m=n*a)
  else:
    n = float(request.args['fnum'])
    a = float(request.args['snum'])
    createtableifnot()
    insert(request.method, n, a, n a, n-a, n/a, n*a)
    return jsonify(Sum=n a, Difference=n-a, Division=n/a, Multiplication=n*a)

@app.route('/printdata')
def pd():
  d = printdata()
  return str(d)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

