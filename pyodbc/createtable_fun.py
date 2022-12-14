import pyodbc

def conn():
  server = 'remotemysql.com'
  database = 'vsF4Cfo0Ne'
  username = 'vsF4Cfo0Ne'
  password = 'Qkk0UXYn7W'
  mystring='DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password

  cnxn = pyodbc.connect(mystring)
  cursor = cnxn.cursor()
  return cursor

def exec(query):
  c = conn()
  c.execute(query)
  return c

#query = "CREATE TABLE IF NOT EXISTS AVINASH_STATS (state varchar(50) NOT NULL,cases INT NOT NULL,PRIMARY KEY(state));"
#query = "DROP TABLE AVINASH_STATS"
#c = exec(query)
#qu = "INSERT INTO Pramodh_STATS VALUES('Maharastra', 6611078), ('Kerala', 4968657), ('Karnataka', 2988333), ('Tamil Nadu', 2702623), ('Andra Pradesh', 2066450), ('Uttar Pradesh', 1710158), ('West Bengal', 1592908), ('Delhi', 1439870), ('Odisha', 1041457), ('Chhattisgarh', 1006052), ('Rajasthan', 954429);"
#cursor.execute(qu)
#cursor.commit()

query = "SHOW tables;"
c = exec(query)
c.execute(query)
#print(c.fetchall())
d = c.fetchone()
while d:
  print(d)
  d = c.fetchone()

#q2="SELECT * FROM AVINASH_STATS"
#c = exec(q2)
#row = c.fetchone()
#while row:
#  print (row)
#  row = c.fetchone()
