import pyodbc
server = 'remotemysql.com'
database = 'vsF4Cfo0Ne'
username = 'vsF4Cfo0Ne'
password = 'Qkk0UXYn7W'
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER='+server+';DATABASE='+database+' ;UID='+username+';PWD='+password)
cursor = cnxn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS AVINASH_STATS (state varchar(50) NOT NULL,cases INT NOT NULL,PRIMARY KEY(state));")

cursor.commit()

query = "SHOW TABLES;"

cursor.execute(query)

d = cursor.fetchone()

while d:
  print(d)
  d = cursor.fetchone()
