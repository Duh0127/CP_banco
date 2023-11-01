import random
import csv
from faker import Faker
from datetime import datetime
from pegar_unid_consulta import pegar_ids
 
fake = Faker("pt_BR")
 
data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1
 
# Nome do arquivo CSV de saída
output_file = 'dados_prescricao_medica.csv'
 
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID_PRESCRICAO_MEDICA', 'ID_MEDICAMENTO', 'DS_POSOLOGIA', 'DS_VIA', 'DS_OBSERVACAO_USO', 'QT_MEDICAMENTO', 'ID_UNID_HOSPITAL', 'ID_CONSULTA']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
 
    for _ in range(499999):
        id_prescricao_medica = id_counter
        id_medicamento = random.randint(1, 150000)
        ds_posologia = fake.sentence(nb_words=4)
        ds_via = random.choice(["ORAL","PARENTAL","SUBCUTÂNEA","NASAL","RETAL","INTRA-VESICAL","NEBULIZAÇÃO","OCULAR"])
        observacao_uso = fake.sentence(nb_words=6)
        qt_medicamento = random.randint(1, 60)
 
        # Suponho que você já tenha uma função pegar_ids definida em 'pegar_unid_consulta.py'
        id_unid_hospital, id_consulta = pegar_ids(id_counter)
 
        writer.writerow({
            'ID_PRESCRICAO_MEDICA': id_prescricao_medica,
            'ID_MEDICAMENTO': id_medicamento,
            'DS_POSOLOGIA': ds_posologia,
            'DS_VIA': ds_via,
            'DS_OBSERVACAO_USO': observacao_uso,
            'QT_MEDICAMENTO': qt_medicamento,
            'ID_UNID_HOSPITAL': id_unid_hospital,
            'ID_CONSULTA': id_consulta
        })
 
        print(id_prescricao_medica, id_medicamento, ds_posologia, ds_via, observacao_uso, qt_medicamento, id_unid_hospital, id_consulta)
 
        id_counter += 1
 
print(f'Dados gravados em {output_file}')