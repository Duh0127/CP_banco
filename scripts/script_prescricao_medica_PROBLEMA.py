from datetime import datetime
import random
import oracledb
from faker import Faker
from pegar_unid_consulta import pegar_ids

fake = Faker("pt_BR")
conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1

for _ in range(499999):
    id_prescricao_medica = id_counter
    id_medicamento = random.randint(1, 150000)
    ds_posologia = fake.sentence(nb_words=4)
    ds_via = random.choice(["ORAL","PARENTAL","SUBCUTÂNEA","NASAL","RETAL","INTRA-VESICAL","NEBULIZAÇÃO","OCULAR"])
    observacao_uso = fake.sentence(nb_words=6)
    qt_medicamento = random.randint(1, 60)

    cur.execute("SELECT ID_CONSULTA, ID_UNID_HOSPITAL FROM T_RHSTU_CONSULTA WHERE ID_CONSULTA = :ID_CONSULTA", ID_CONSULTA=id_counter)
    result = cur.fetchone()
    
    id_unid_hospital = result[1]
    id_consulta = result[0]

    print(id_prescricao_medica, id_medicamento, ds_posologia, ds_via, observacao_uso, qt_medicamento,  id_unid_hospital, id_consulta)

    cur.execute(
        "INSERT INTO T_RHSTU_PRESCRICAO_MEDICA VALUES(:ID_PRESCRICAO_MEDICA, :ID_UNID_HOSPITAL, :ID_CONSULTA, :ID_MEDICAMENTO, :DS_POSOLOGIA, :DS_VIA, :DS_OBSERVACAO_USO, :QT_MEDICAMENTO, USER, SYSDATE)",
        ID_PRESCRICAO_MEDICA=id_counter,
        ID_UNID_HOSPITAL=id_unid_hospital,
        ID_CONSULTA=id_consulta,
        ID_MEDICAMENTO=id_medicamento,
        DS_POSOLOGIA=ds_posologia,
        DS_VIA=ds_via,
        DS_OBSERVACAO_USO=observacao_uso,
        QT_MEDICAMENTO=qt_medicamento
    )
    
    print(id_counter)
    id_counter += 1

conn.commit()
cur.close()
conn.close()