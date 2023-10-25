import random
import oracledb
from faker import Faker

conn = oracledb.connect( user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl" )
cur = conn.cursor()
fake = Faker("pt-BR")

id_contato_counter = 1
tipos_contato = [1, 2, 3, 4, 5, 6]

for _ in range(500000):
    id_paciente = random.randint(1, 500000)
    id_contato = id_contato_counter
    id_tipo_contato = random.choice(tipos_contato)
    nm_contato = fake.first_name() + " " + fake.last_name()
    nr_ddi = None
    nr_ddd = None
    nr_telefone = None

    if random.choice([True, False]):
        nr_ddi = fake.random_int(min=1, max=999)
        nr_ddd = fake.random_int(min=1, max=999)
        nr_telefone = f"{random.randint(1000, 9999)}{random.randint(1000, 9999)}"

    cur.execute(
        """INSERT INTO T_RHSTU_CONTATO_PACIENTE (ID_PACIENTE, ID_CONTATO, ID_TIPO_CONTATO, NM_CONTATO, NR_DDI, NR_DDD, NR_TELEFONE, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_PACIENTE, :ID_CONTATO, :ID_TIPO_CONTATO, :NM_CONTATO, :NR_DDI, :NR_DDD, :NR_TELEFONE, SYSDATE, USER)""",
        ID_PACIENTE=id_paciente,
        ID_CONTATO=id_contato,
        ID_TIPO_CONTATO=id_tipo_contato,
        NM_CONTATO=nm_contato,
        NR_DDI=nr_ddi,
        NR_DDD=nr_ddd,
        NR_TELEFONE=nr_telefone,
    )
    print(f"Inserted {id_contato_counter} of 500000")
    id_contato_counter += 1

conn.commit()
cur.close()
conn.close()
