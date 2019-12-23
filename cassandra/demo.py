from cassandra.cluster import Cluster


# https://docs.datastax.com/en/developer/python-driver/3.20/getting_started/

cluster = Cluster(['192.168.110.231'], port=9042)
session = cluster.connect() # session = cluster.connect("users") session.set_keyspace('users') or session.execute('USE users')
session.execute('CREATE KEYSPACE democloud')
# DROP KEYSPACE “KeySpace name”
session.set_keyspace('democloud') # or session.execute('USE users')
# DROP TABLE emp;
'''
CREATE TABLE users(
   emp_id int PRIMARY KEY,
   emp_name text,
   emp_city text,
   emp_sal varint,
   emp_phone varint
   );
'''


rows = session.execute('SELECT name, age, email FROM users')
for user_row in rows:
    print (user_row.name, user_row.age, user_row.email)

session.execute("INSERT INTO USERS (name, age) VALUES (%s, %s)", ("bob", 42))

for (name, age, email) in rows:
    print (name, age, email)