from datetime import datetime
import random
from faker import Faker
import oracledb

fake = Faker('pt_BR')

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

# Data mínima e máxima para as datas de início
data_min = datetime(2010, 1, 1)
data_max = datetime(2022, 12, 31)

# Contador para ID do paciente
id_counter = 1

def gerar_letra_aleatoria():
    letras_possiveis = ['A', 'C', 'P']
    letra_aleatoria = random.choice(letras_possiveis)
    return letra_aleatoria

# Quantidade de registros a serem criados
for _ in range(500000):
    id_consulta_pagto = id_counter 
    id_consulta = id_counter 
    id_paciente = id_counter 
   

    cur.execute("SELECT ID_UNID_HOSPITAL FROM T_RHSTU_CONSULTA WHERE ID_CONSULTA = :ID_CONSULTA", ID_CONSULTA = id_consulta)
    # Recupere o dado do SELECT
    dado_selecionado = cur.fetchone()

    id_unid_hospital = dado_selecionado[0]
    print(dado_selecionado[0])

    cur.execute("SELECT ID_PACIENTE_PS FROM T_RHSTU_PACIENTE_PLANO_SAUDE WHERE ID_PACIENTE = :ID_PACIENTE", ID_PACIENTE = id_paciente)
    # Recupere o dado do SELECT
    dado_selecionado = cur.fetchone()
    print(dado_selecionado[0])
    
    id_paciente_ps = dado_selecionado[0]
    id_forma_pagto = random.randint(1, 6)
    dt_pagto_consulta = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
    st_pagto_consulta = gerar_letra_aleatoria()




    dt_fim = None
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"
    
    cur.execute(
        """INSERT INTO T_RHSTU_CONSULTA_FORMA_PAGTO (ID_CONSULTA_FORMA_PAGTO, ID_UNID_HOSPITAL, ID_CONSULTA, ID_PACIENTE_PS, ID_FORMA_PAGTO, DT_PAGTO_CONSULTA, ST_PAGTO_CONSULTA, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_CONSULTA_FORMA_PAGTO, :ID_UNID_HOSPITAL, :ID_CONSULTA, :ID_PACIENTE_PS, :ID_FORMA_PAGTO, :DT_PAGTO_CONSULTA, :ST_PAGTO_CONSULTA, SYSDATE, USER)""",
        ID_CONSULTA_FORMA_PAGTO = id_consulta_pagto, 
        ID_UNID_HOSPITAL = id_unid_hospital, 
        ID_CONSULTA = id_consulta, 
        ID_PACIENTE_PS = id_paciente_ps, 
        ID_FORMA_PAGTO = id_forma_pagto, 
        DT_PAGTO_CONSULTA = dt_pagto_consulta, 
        ST_PAGTO_CONSULTA = st_pagto_consulta
    )
    print(id_counter)
    id_counter += 1

conn.commit()
cur.close()
conn.close()
