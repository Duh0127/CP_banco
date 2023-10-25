from datetime import datetime
import random
import oracledb
from faker import Faker

fake = Faker("pt_BR")
conn = oracledb.connect(
    user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl"
)
cur = conn.cursor()

data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1

for _ in range(1, 10):
    id_prescricao_medica = id_counter
    id_unid_hospital = random.randint(1, 20000)
    id_consulta = id_unid_hospital
    id_medicamento = random.randint(1, 150000)
    ds_posologia = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    ds_via = random.choice(
        [
            "ORAL",
            "PARENTAL",
            "SUBCUTÂNEA",
            "NASAL",
            "RETAL",
            "INTRA-VESICAL",
            "NEBULIZAÇÃO",
            "OCULAR",
        ]
    )

    print("ID_PRESCRICAO_MEDICA: " + str(id_prescricao_medica))
    print("ID_UNID_HOSPITAL: " + str(id_unid_hospital))
    print("ID_CONSULTA: " + str(id_consulta))
    print("ID_MEDICAMENTO: " + str(id_medicamento))
    print("DS_POSOLOGIA: " + ds_posologia)
    print("DS_VIA: " + ds_via)

    cur.execute(
        """INSERT INTO T_RHSTU_PRESCRICAO_MEDICA 
            (
                ID_PRESCRICAO_MEDICA, 
                ID_UNID_HOSPITAL, 
                ID_CONSULTA, 
                ID_MEDICAMENTO,
                DS_POSOLOGIA, 
                DS_VIA, 
                DS_OBSERVACAO_USO, 
                QT_MEDICAMENTO, 
                NM_USUARIO, 
                DT_CADASTRO
            )
            VALUES
            (
                :ID_PRESCRICAO_MEDICA, 
                :ID_UNID_HOSPITAL, 
                :ID_CONSULTA, 
                :ID_MEDICAMENTO, 
                :DS_POSOLOGIA, 
                :DS_VIA, 
                NULL, 
                NULL, 
                USER, 
                SYSDATE
            )""",
        ID_PRESCRICAO_MEDICA=id_prescricao_medica,
        ID_UNID_HOSPITAL=id_unid_hospital,
        ID_CONSULTA=id_consulta,
        ID_MEDICAMENTO=id_medicamento,
        DS_POSOLOGIA=ds_posologia,
        DS_VIA=ds_via,
    )
    print(id_counter)
    id_counter += 1

conn.commit()
cur.close()
conn.close()
