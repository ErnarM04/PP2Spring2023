import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='Phonebook',
    user='postgres',
    password='20112004erkow',
    port='6566'
)

cur = conn.cursor()

cur.execute("CREATE TABLE phonebook (name VARCHAR(50), phone VARCHAR(20))")

conn.commit()
cur.close()
conn.close()