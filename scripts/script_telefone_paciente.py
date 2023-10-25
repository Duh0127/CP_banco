from datetime import datetime
import random
import oracledb

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

# Função para gerar números de telefone aleatórios
def generate_phone_number():
    ddi = random.randint(1, 99)
    ddd = random.randint(10, 99)
    number = ''.join(random.choice("0123456789") for _ in range(8))
    return ddi, ddd, number

# Contador para ID de telefone
id_counter = 1

# Quantidade de telefones a serem criados
for _ in range(500000):
    id_paciente = random.randint(1, 500000)
    nr_ddi, nr_ddd, nr_telefone = generate_phone_number()
    tp_telefone = random.choice(["COMERCIAL", "RESIDENCIAL", "CONTATO OU RECADO", "CELULAR"])
    st_telefone = random.choice(["A", "I"])
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"

    cur.execute(
        """INSERT INTO T_RHSTU_TELEFONE_PACIENTE
           (ID_TELEFONE, ID_PACIENTE, NR_DDI, NR_DDD, NR_TELEFONE, TP_TELEFONE, ST_TELEFONE, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_TELEFONE, :ID_PACIENTE, :NR_DDI, :NR_DDD, :NR_TELEFONE, :TP_TELEFONE, :ST_TELEFONE, SYSDATE, USER)""",
        ID_TELEFONE=id_counter,
        ID_PACIENTE=id_paciente,
        NR_DDI=nr_ddi,
        NR_DDD=nr_ddd,
        NR_TELEFONE=nr_telefone,
        TP_TELEFONE=tp_telefone,
        ST_TELEFONE=st_telefone,
    )
    id_counter += 1
    print(id_counter)

conn.commit()
cur.close()
conn.close()
