import mysql.connector

config = {
  'user': 'root',
  'password': 'rasengan',
  'host': 'localhost',
  'database': 'library',
}

conn = mysql.connector.connect(**config)
cursor=conn.cursor()
cursor.execute('''select * from author''')
res=cursor.fetchall()
print(type(res))
print(res[:100])


conn.commit()