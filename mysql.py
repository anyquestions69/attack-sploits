
import MySQLdb
import sys

IP = sys.argv[1]
PORT = 3306

USER = 'redcadet'
PASSWORD = 'secretpass'
DATABASE = 'redcadet'

conn = MySQLdb.connect(host=IP, port=PORT, user=USER, passwd=PASSWORD, db=DATABASE)
cursor = conn.cursor()

query = f'''SELECT DISTINCT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA="{DATABASE}"'''
cursor.execute(query)

tables = cursor.fetchall()

for table, in tables:
    query = f'''SELECT * from {table}'''
    cursor.execute(query)
    rows = cursor.fetchmany(1000)
    while rows:
        print(rows, flush=True)
        rows = cursor.fetchmany(1000)