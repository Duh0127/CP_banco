import random
import oracledb
from faker import Faker
from datetime import datetime

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()
fake = Faker("pt-BR")

start_date = datetime(2000, 1, 1)
end_date = datetime(2022, 12, 31)

id_hospital_endereco_counter = 1

for _ in range(20000):
    cur.execute("SELECT ID_UNID_HOSPITAL FROM T_RHSTU_UNID_HOSPITALAR WHERE ID_UNID_HOSPITAL = :ID", ID=id_hospital_endereco_counter)
    id_unid_hosp = cur.fetchone()[0]
    id_logradouro = random.randint(1, 10000)
    nr_logradouro = random.randint(1, 50000)
    ds_complemento_numero = None
    ds_ponto_referencia = None
    dt_inicio = fake.date_time_between(start_date=start_date, end_date=end_date)

    cur.execute(
        """INSERT INTO T_RHSTU_ENDERECO_UNIDHOSP
       (
           ID_END_UNIDHOSP, 
           ID_UNID_HOSPITAL,
           ID_LOGRADOURO, 
           NR_LOGRADOURO, 
           DS_COMPLEMENTO_NUMERO, 
           DS_PONTO_REFERENCIA, 
           DT_INICIO, 
           DT_FIM, 
           DT_CADASTRO, 
           NM_USUARIO
       )
       VALUES
       (
           :ID_END_UNIDHOSP, 
           :ID_UNID_HOSP,  -- Correct parameter name
           :ID_LOGRADOURO, 
           :NR_LOGRADOURO, 
           :DS_COMPLEMENTO_NUMERO, 
           :DS_PONTO_REFERENCIA, 
           :DT_INICIO, 
           NULL, 
           SYSDATE, 
           USER
       )""",
        ID_END_UNIDHOSP=id_hospital_endereco_counter,
        ID_UNID_HOSP=id_unid_hosp,
        ID_LOGRADOURO=id_logradouro,
        NR_LOGRADOURO=nr_logradouro,
        DS_COMPLEMENTO_NUMERO=ds_complemento_numero,
        DS_PONTO_REFERENCIA=ds_ponto_referencia,
        DT_INICIO=dt_inicio,
    )

    print(f"Inserted {id_hospital_endereco_counter} of 20000")
    id_hospital_endereco_counter += 1

conn.commit()
cur.close()
conn.close()
