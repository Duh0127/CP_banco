import random
import csv
from faker import Faker
from datetime import datetime
 
fake = Faker('pt_BR')
 
data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 500000
 
# Nome do arquivo CSV de saída
output_file = 'D:/dados_consultasFOI2.csv'
 
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID_UNID_HOSPITAL', 'ID_CONSULTA', 'ID_PACIENTE', 'ID_FUNC', 'DT_HR_CONSULTA', 'NR_CONSULTORIO', 'DT_CADASTRO', 'NM_USUARIO']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
 
    for _ in range(3000000):
        id_unid_hospital = random.randint(1, 20000)
        id_consulta = id_counter
        id_paciente = random.randint(1, 500000)
        id_funcionario = random.randint(1, 61000)
        dt_hr_consulta = fake.date_time_between_dates(data_min, data_max).strftime('%Y-%m-%d:%H:%M:%S')
 
        nr_consultorio = random.randint(1, 99999)
        dt_cadastro = datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
        nm_usuario = "RM552164"
    
 
        writer.writerow({
            'ID_UNID_HOSPITAL': id_unid_hospital,
            'ID_CONSULTA': id_consulta,
            'ID_PACIENTE': id_paciente,
            'ID_FUNC': id_funcionario,
            'DT_HR_CONSULTA': dt_hr_consulta,
            'NR_CONSULTORIO': nr_consultorio,
            'DT_CADASTRO': dt_cadastro,
            'NM_USUARIO': nm_usuario

        })
 
        print(id_counter)
        id_counter += 1
 
print(f'Dados gravados em {output_file}')