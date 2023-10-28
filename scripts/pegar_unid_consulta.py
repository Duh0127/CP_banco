import oracledb

def pegar_ids():
    conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
    cur = conn.cursor()
    ids = []

    for id_counter in range(1, 10):
        cur.execute("SELECT ID_CONSULTA, ID_UNID_HOSPITAL FROM T_RHSTU_CONSULTA WHERE ID_CONSULTA = :ID_CONSULTA", ID_CONSULTA=id_counter)
        result = cur.fetchone()
        ids.append(result)
    
    conn.close()
    return ids
