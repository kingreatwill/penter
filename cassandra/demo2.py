from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

rows = session.execute('SELECT cluster_name, listen_address FROM system.local')
for row in rows:
    print (row.cluster_name, row.listen_address)