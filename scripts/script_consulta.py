from datetime import datetime
import random
import oracledb
from faker import Faker

fake = Faker('pt_BR')
conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1

for _ in range(1, 500000):
    id_unid_hospital = random.randint(1, 20000)
    id_consulta = id_counter
    id_paciente = id_counter
    id_funcionario = random.randint(1, 61000)
    dt_hr_consulta = fake.date_time_between_dates(data_min, data_max).strftime('%d-%b-%Y %H:%M:%S').upper()
    nr_consultorio = random.randint(1, 99999)
    
    cur.execute(
        """INSERT INTO T_RHSTU_CONSULTA (ID_UNID_HOSPITAL, ID_CONSULTA, ID_PACIENTE, ID_FUNC, DT_HR_CONSULTA, NR_CONSULTORIO, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_UNID_HOSPITAL, :ID_CONSULTA, :ID_PACIENTE, :ID_FUNC, TO_DATE(:DT_HR_CONSULTA, 'DD-MON-YYYY HH24:MI:SS'), :NR_CONSULTORIO, SYSDATE, USER)""",
        ID_UNID_HOSPITAL=id_unid_hospital,
        ID_CONSULTA=id_consulta,
        ID_PACIENTE=id_paciente,
        ID_FUNC=id_funcionario,
        DT_HR_CONSULTA=dt_hr_consulta,
        NR_CONSULTORIO=nr_consultorio
    )
    print(id_counter)
    id_counter += 1

conn.commit()
cur.close()
conn.close()
