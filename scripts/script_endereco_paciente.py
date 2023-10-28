import random
import oracledb
from faker import Faker

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()
fake = Faker("pt-BR")

id_endereco_counter = 1

for _ in range(500000):
    id_paciente = random.randint(1, 500000)
    id_logradouro = random.randint(1, 10000)
    nr_logradouro = fake.building_number()
    ds_complemento_numero = fake.building_number()
    ds_ponto_referencia = fake.sentence(nb_words=3)
    dt_inicio = fake.date_time_between(start_date='-1y', end_date='now')
    
    cur.execute(
        """INSERT INTO T_RHSTU_ENDERECO_PACIENTE
           (
               ID_ENDERECO, 
               ID_PACIENTE, 
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
               :ID_ENDERECO, 
               :ID_PACIENTE, 
               :ID_LOGRADOURO, 
               :NR_LOGRADOURO, 
               :DS_COMPLEMENTO_NUMERO, 
               :DS_PONTO_REFERENCIA, 
               :DT_INICIO, 
               NULL, 
               SYSDATE, 
               USER
           )""",
        ID_ENDERECO=id_endereco_counter,
        ID_PACIENTE=id_paciente,
        ID_LOGRADOURO=id_logradouro,
        NR_LOGRADOURO=nr_logradouro,
        DS_COMPLEMENTO_NUMERO=ds_complemento_numero,
        DS_PONTO_REFERENCIA=ds_ponto_referencia,
        DT_INICIO=dt_inicio,
    )
    print(f"Inserted {id_endereco_counter} of 500000")
    id_endereco_counter += 1

conn.commit()
cur.close()
conn.close()
