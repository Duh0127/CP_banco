from datetime import datetime
import random
import oracledb

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

id_counter = 1
especialidades = ["Cardiologia", "Dermatologia", "Ortopedia", "Pediatria", "Oncologia", "Ginecologia", "Neurologia", "Urologia", "Oftalmologia"]

for _ in range(8000):
    nr_crm = f"{random.randint(10000, 99999)}{random.randint(100, 999)}"
    ds_especialidade = random.choice(especialidades)
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"
    
    cur.execute(
        """INSERT INTO T_RHSTU_MEDICO (ID_FUNC, NR_CRM, DS_ESPECIALIDADE, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_FUNC, :NR_CRM, :DS_ESPECIALIDADE, SYSDATE, USER)""",
        ID_FUNC=id_counter,
        NR_CRM=nr_crm,
        DS_ESPECIALIDADE=ds_especialidade
    )
    print(f"Inserted {id_counter} {nr_crm} {ds_especialidade}")
    id_counter += 1

conn.commit()
cur.close()
conn.close()
