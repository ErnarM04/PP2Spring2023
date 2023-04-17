import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='Snake',
    user='postgres',
    password='20112004erkow',
    port = '6566'
    )

cur = conn.cursor()
cur.execute("SELECT * FROM Scores")
rows = cur.fetchall()
cur.close()
for row in rows:
    print(row)