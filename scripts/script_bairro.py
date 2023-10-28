import random
import oracledb
from faker import Faker

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()
fake = Faker("pt-BR")

id_logradouro_counter = 1

for _ in range(10000):
    id_bairro = random.choice([x for x in range(1, 714) if x != 11])
    nm_logradouro = fake.street_name()
    nr_cep = random.randint(10000000, 99999999)

    print(f"ID_BAIRRO: {id_bairro}")
    print(f"NM_LOGRADOURO: {nm_logradouro}")
    print(f"NR_CEP: {nr_cep}")

    cur.execute(
        """INSERT INTO T_RHSTU_LOGRADOURO
           (
               ID_LOGRADOURO, 
               ID_BAIRRO, 
               NM_LOGRADOURO, 
               NR_CEP, 
               DT_CADASTRO, 
               NM_USUARIO
           )
           VALUES
           (
               :ID_LOGRADOURO, 
               :ID_BAIRRO, 
               :NM_LOGRADOURO, 
               :NR_CEP, 
               SYSDATE, 
               USER
           )""",
        ID_LOGRADOURO=id_logradouro_counter,
        ID_BAIRRO=id_bairro,
        NM_LOGRADOURO=nm_logradouro,
        NR_CEP=nr_cep,
    )
    print(f"Inserted {id_logradouro_counter} of 10000")
    id_logradouro_counter += 1

conn.commit()
cur.close()
conn.close()
