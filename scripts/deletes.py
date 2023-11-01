import oracledb

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()



conn.commit()
cur.close()
conn.close()