
import random
import csv
from faker import Faker
from datetime import datetime
 
fake = Faker('pt_BR')
 
data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1
 
# Nome do arquivo CSV de saída
output_file = 'D:/dados_medicamento2.csv'
 
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID_MEDICAMENTO', 'NM_MEDICAMENTO', 'DS_DETALHADA_MEDICAMENTO', 'NR_CODIGO_BARRAS', 'DT_CADASTRO', 'NM_USUARIO']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
 
    for _ in range(3000000):

        nm_medicamento = fake.word()
        ds_detalhada_medicamento = fake.paragraph()
        nr_codigo_barras = random.randint(100000000000, 999999999999)
        dt_cadastro = datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
        nm_usuario = "RM552164"
    
 
        writer.writerow({
            'ID_MEDICAMENTO':id_counter,
            'NM_MEDICAMENTO':nm_medicamento,
            'DS_DETALHADA_MEDICAMENTO':ds_detalhada_medicamento,
            'NR_CODIGO_BARRAS':nr_codigo_barras,
            'DT_CADASTRO': dt_cadastro,
            'NM_USUARIO': nm_usuario

        })
 
        print(id_counter)
        id_counter += 1
 
print(f'Dados gravados em {output_file}')