from datetime import datetime
import random
import oracledb
from faker import Faker

fake = Faker('pt_BR')
conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

id_counter = 8001
for _ in range(3000):
    nr_cnh = f"{random.randint(10000000, 99999999)}"
    nm_categoria_cnh = random.choice(["B", "C", "D", "E"])
    dt_validade_cnh = fake.date_between_dates(datetime(1980, 1, 1), datetime(2023, 12, 31)).strftime('%d-%b-%Y').upper()
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"
    
    cur.execute(
        """INSERT INTO T_RHSTU_MOTORISTA (ID_FUNC, NR_CNH, NM_CATEGORIA_CNH, DT_VALIDADE_CNH, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_FUNC, :NR_CNH, :NM_CATEGORIA_CNH, TO_DATE(:DT_VALIDADE_CNH, 'DD-MON-YYYY'), SYSDATE, USER)""",
        ID_FUNC=id_counter,
        NR_CNH=nr_cnh,
        NM_CATEGORIA_CNH=nm_categoria_cnh,
        DT_VALIDADE_CNH=dt_validade_cnh
    )
    print(f"Inserted {id_counter}")
    id_counter += 1

conn.commit()
cur.close()
conn.close()
