from cassandra.cluster import Cluster


# https://docs.datastax.com/en/developer/python-driver/3.20/getting_started/

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect() # session = cluster.connect("users") session.set_keyspace('users') or session.execute('USE users')
session.execute("CREATE KEYSPACE IF NOT EXISTS democloud  WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3}")
# DROP KEYSPACE “KeySpace name”
session.set_keyspace('democloud') # or session.execute('USE users')
# DROP TABLE emp;

# session.execute('''
# CREATE TABLE users(
#    emp_id int PRIMARY KEY,
#    emp_name text,
#    emp_city text,
#    emp_sal varint,
#    emp_phone varint
#    )
# ''')


rows = session.execute('SELECT emp_name, emp_id, emp_sal FROM users')
for user_row in rows:
    print (user_row.emp_name, user_row.emp_id, user_row.emp_sal)

session.execute("INSERT INTO USERS (emp_id, emp_name, emp_city) VALUES (%s, %s, %s)", (3, "bob", "42"))

rows = session.execute('SELECT emp_name, emp_id, emp_sal FROM users')
for (emp_name, emp_id, emp_sal) in rows:
    print (emp_name, emp_id, emp_sal)