import random
import oracledb
from faker import Faker

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()
fake = Faker()

id_counter = 1
for _ in range(150000):
    nm_medicamento = fake.word()
    ds_detalhada_medicamento = fake.paragraph()
    nr_codigo_barras = random.randint(100000000000, 999999999999)
    
    cur.execute(
        """INSERT INTO T_RHSTU_MEDICAMENTO (ID_MEDICAMENTO, NM_MEDICAMENTO, DS_DETALHADA_MEDICAMENTO, NR_CODIGO_BARRAS, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_MEDICAMENTO, :NM_MEDICAMENTO, :DS_DETALHADA_MEDICAMENTO, :NR_CODIGO_BARRAS, SYSDATE, USER)""",
        ID_MEDICAMENTO=id_counter,
        NM_MEDICAMENTO=nm_medicamento,
        DS_DETALHADA_MEDICAMENTO=ds_detalhada_medicamento,
        NR_CODIGO_BARRAS=nr_codigo_barras
    )
    print("Medicamento ", id_counter)
    id_counter += 1

conn.commit()
cur.close()
conn.close()
