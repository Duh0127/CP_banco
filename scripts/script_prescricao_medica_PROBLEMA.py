import random
import csv
from faker import Faker
import datetime
 
fake = Faker('pt_BR')
 
data_min = datetime.datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime.datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1
 
# Nome do arquivo CSV de saída
output_file = 'D:/dados_prescricao.csv'
 
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID_UNID_HOSPITAL', 'ID_CONSULTA', 'ID_PACIENTE', 'ID_FUNC', 'DT_HR_CONSULTA', 'NR_CONSULTORIO']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
 
    for _ in range(1, 10000000):
        id_unid_hospital = random.randint(1, 20000)
        id_consulta = id_counter
        id_paciente = id_counter
        id_funcionario = random.randint(1, 61000)
        dt_hr_consulta = fake.date_time_between_dates(data_min, data_max).strftime('%d-%b-%Y %H:%M:%S').upper()
        nr_consultorio = random.randint(1, 99999)
 
        writer.writerow({
            'ID_UNID_HOSPITAL': id_unid_hospital,
            'ID_CONSULTA': id_consulta,
            'ID_PACIENTE': id_paciente,
            'ID_FUNC': id_funcionario,
            'DT_HR_CONSULTA': dt_hr_consulta,
            'NR_CONSULTORIO': nr_consultorio
        })
 
        print(id_counter)
        id_counter += 1
 
print(f'Dados gravados em {output_file}')