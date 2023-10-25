from datetime import datetime
import random
import string
import oracledb

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

# Função para gerar e-mails aleatórios
def generate_email():
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "fiap.com.br", "hotmail.com", "uol.com.br", "bol.com.br", "msn.com", "yahoo.com.br", "ig.com"])
    username = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    return f"{username}@{domain}"

# Contador para ID de e-mail
id_counter = 1

# Quantidade de e-mails a serem criados
for _ in range(500000):
    id_paciente = random.randint(1, 500000)
    ds_email = generate_email()
    tp_email = random.choice(["Pessoal", "Profissional"])
    st_email = random.choice(["A", "I"])
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"

    cur.execute(
        """INSERT INTO T_RHSTU_EMAIL_PACIENTE
           (ID_EMAIL, ID_PACIENTE, DS_EMAIL, TP_EMAIL, ST_EMAIL, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_EMAIL, :ID_PACIENTE, :DS_EMAIL, :TP_EMAIL, :ST_EMAIL, SYSDATE, USER)""",
        ID_EMAIL=id_counter,
        ID_PACIENTE=id_paciente,
        DS_EMAIL=ds_email,
        TP_EMAIL=tp_email,
        ST_EMAIL=st_email,
    )
    id_counter += 1
    print(id_counter)

conn.commit()
cur.close()
conn.close()
