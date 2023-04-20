import psycopg2

conn = psycopg2.connect(host="localhost",
                        database="Snake",
                        user="postgres",
                        password="20112004erkow",
                        port="6566")

cur = conn.cursor()

cur.execute("CREATE TABLE Scores (nickname VARCHAR(255), score integer)")

conn.commit()

cur.close()
conn.close()