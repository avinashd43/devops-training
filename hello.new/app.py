#comment
from flask import Flask, render_template, request, jsonify

application = Flask(__name__)

def db_conn():
    import pyodbc

    #server = 'remotemysql.com'
    #database = 'Qj6fi1rKNM'
    #username = 'Qj6fi1rKNM'
    #password = 'VAA9GtgapG'

    server = 'db4free.net'
    database = 'mysql9753'
    username = 'myuser9753'
    password = 'mypass9753'

    conn = 'DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

    cnxn = pyodbc.connect(conn)
    cursor = cnxn.cursor()
    return cursor

def createtable():
    cursor = db_conn()

    cursor.execute("CREATE TABLE IF NOT EXISTS SAGAR_EMPLOYEEDB(eid varchar(10) NOT NULL, ename varchar(20) NOT NULL, esalary INT NOT NULL, PRIMARY KEY(eid));")
    cursor.close()

def checkrecord(eid):
    cursor = db_conn()

    cursor.execute("SELECT * FROM SAGAR_EMPLOYEEDB WHERE eid=" + eid +";")
    row = cursor.fetchone()
    n = 0

    if row is not None:
        if len(row) > 1:
            n = 1
    cursor.close()
    return n

def addrecord(df):
    import pandas

    cursor = db_conn()

    for index, row in df.iterrows():
        cursor.execute("INSERT INTO SAGAR_EMPLOYEEDB VALUES(?,?,?)", row.eid, row.ename, row.esalary)
    cursor.commit()
    cursor.close()

def getdata():
    import pyodbc
    import pandas as pd

    server = 'remotemysql.com'
    database = 'Qj6fi1rKNM'
    username = 'Qj6fi1rKNM'
    password = 'VAA9GtgapG'

    conn = 'DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

    cnxn = pyodbc.connect(conn)
    cursor = cnxn.cursor()

    query = "SELECT * FROM SAGAR_EMPLOYEEDB;"
    df = pd.read_sql(query, cnxn)
    return df

@application.route('/')
def hello():
    return render_template('index.html')

@application.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        eid = request.form['eid']
        ename = request.form['ename']
        esalary = request.form['esalary']

        import pandas as pd
        data={
            "eid": [eid],
            "ename": [ename],
            "esalary": [esalary]
        }
        df = pd.DataFrame(data)

        createtable()
        n = checkrecord(eid)

        if n == 0:
          addrecord(df)

        df = getdata()
        df1 = df.to_html(border="0", classes="table", index_names=False, justify='start')
        print (df1)
        return render_template('result.html', cr=df1)
    elif request.method == 'GET':
        eid = request.args['eid']
        ename = request.args['ename']
        esalary = request.args['esalary']

        import pandas as pd
        data={
            "eid": [eid],
            "ename": [ename],
            "esalary": [esalary]
        }
        df = pd.DataFrame(data)

        createtable()
        n = checkrecord(eid)

        if n == 0:
          addrecord(df)

        import json
        df = getdata()
        df1 = df.to_json(orient='records')
        x = json.loads(df1)
        return json.dumps(x)
        #return jsonify(Employee=df1)
    else:
        return "Invalid Method"

@application.route('/getone')
def getone():
    return render_template('getone.html')

@application.route('/print', methods=['POST', 'GET'])
def print():
    if request.method == 'POST':
        eid = request.form['eid']

        cursor = db_conn()

        r = 0
        n = checkrecord(eid)
        if n == 1:
            query = "SELECT ename,eid,esalary FROM SAGAR_EMPLOYEEDB WHERE eid="+eid+";"
            cursor.execute(query)
            r = cursor.fetchone()
        return render_template('printresult.html', n=r[0], i=r[1], s=r[2])
    elif request.method == 'GET':
        eid = request.args['eid']
        cursor = db_conn()

        r = 0
        n = checkrecord(eid)
        if n == 1:
            query = "SELECT ename,eid,esalary FROM SAGAR_EMPLOYEEDB WHERE eid="+eid+";"
            cursor.execute(query)
            r = cursor.fetchone()
        return jsonify(Name=r[0], ID=r[1], Salary=r[2])
    else:
        return "Invalid Method"

@application.route('/delone')
def delone():
    return render_template('delone.html')

@application.route('/delprint', methods=['POST', 'GET'])
def delprint():
    if request.method == 'POST':
        eid = request.form['eid']

        cursor = db_conn()

        n = checkrecord(eid)
        if n == 1:
            query = "DELETE FROM SAGAR_EMPLOYEEDB WHERE eid="+eid+";"
            cursor.execute(query)
            cursor.commit()
        df = getdata()
        df1 = df.to_html(border="0", classes="table", index_names=False, justify='start')
        return render_template('result.html', cr=df1)
    elif request.method == 'GET':
        eid = request.args['eid']
        cursor = db_conn()

        n = checkrecord(eid)
        if n == 1:
            query = "DELETE FROM SAGAR_EMPLOYEEDB WHERE eid="+eid+";"
            cursor.execute(query)
            cursor.commit()
        import json
        df = getdata()
        df1 = df.to_json(orient='records')
        x = json.loads(df1)
        return json.dumps(x)
    else:
        return "Invalid Method"

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
