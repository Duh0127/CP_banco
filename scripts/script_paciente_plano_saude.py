from datetime import datetime
import random
from faker import Faker
import oracledb

fake = Faker('pt_BR')

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

# Data mínima e máxima para as datas de início
data_min = datetime(2000, 1, 1)
data_max = datetime(2022, 12, 31)

# Contador para ID do paciente
id_counter = 1

# Quantidade de registros a serem criados
for _ in range(500000):
    id_paciente = random.randint(1, 500000)  # ID de paciente aleatório entre 1 e 50000
    id_plano_saude = random.randint(1, 20)  # ID de plano de saúde aleatório entre 1 e 20, excluindo o número 11
    while id_plano_saude == 11:
        id_plano_saude = random.randint(1, 20)
    nr_carteira_ps = str(random.randint(10000000, 99999999))  # Número de carteirinha de saúde de 8 dígitos
    dt_inicio = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
    dt_fim = None
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"
    
    cur.execute(
        """INSERT INTO T_RHSTU_PACIENTE_PLANO_SAUDE (ID_PACIENTE_PS, ID_PACIENTE, ID_PLANO_SAUDE, NR_CARTEIRA_PS, DT_INICIO, DT_FIM, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_PACIENTE_PS, :ID_PACIENTE, :ID_PLANO_SAUDE, :NR_CARTEIRA_PS, TO_DATE(:DT_INICIO, 'DD-MON-YYYY'), :DT_FIM, SYSDATE, USER)""",
        ID_PACIENTE_PS=id_counter,
        ID_PACIENTE=id_paciente,
        ID_PLANO_SAUDE=id_plano_saude,
        NR_CARTEIRA_PS=nr_carteira_ps,
        DT_INICIO=dt_inicio,
        DT_FIM=dt_fim
    )
    print(id_counter)
    id_counter += 1

conn.commit()
cur.close()
conn.close()
