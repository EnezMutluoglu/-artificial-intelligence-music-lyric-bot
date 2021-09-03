import psycopg2



conn = psycopg2.connect(host="localhost",
                    port="7114",
                    database="deneme",
                    user="postgres",
                    password="145356")
cur = conn.cursor()
print ("Opened database successfully")


comp_schema = """
id SERİAL PRIMARY KEY NOT NULL,
url TEXT,
song TEXT
"""

table_name = 'comp_first'

cur.execute("CREATE TABLE IF NOT EXISTS comp_first (id integer ,url TEXT,song TEXT)")

conn.commit()
conn.close()


