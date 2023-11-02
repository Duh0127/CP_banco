
import random
import csv
from faker import Faker
from datetime import datetime
 
fake = Faker('pt_BR')
 
data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1
 
# Nome do arquivo CSV de saída
output_file = 'D:/dados_FUNCIONARIOS2.csv'
output_file2 = 'D:/dados_MOTORISTA.csv'
output_file3 = 'D:/dados_MED.csv'

with open(output_file3, 'w', newline='', encoding='utf-8') as csvfile3:
        fieldnames3 = ['ID_FUNC',
                'NR_CRM',
                'DS_ESPECIALIDADE',
                'DT_CADASTRO',
                'NM_USUARIO']
        writer3 = csv.DictWriter(csvfile3, fieldnames=fieldnames3)
    
        writer3.writeheader()
    
        fake = Faker('pt_BR') 

        especialidades = ["Cardiologia", "Dermatologia", "Ortopedia", "Pediatria", "Oncologia", "Ginecologia", "Neurologia", "Urologia", "Oftalmologia"]
        for _ in range(1500000):
            nr_crm = f"{random.randint(10000, 99999)}{random.randint(100, 999)}"
            ds_especialidade = random.choice(especialidades)
            dt_cadastro = datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
            nm_usuario = "RM552164"
            

            writer3.writerow({
                
                'ID_FUNC':id_counter,
                'NR_CRM':nr_crm,
                'DS_ESPECIALIDADE':ds_especialidade,
                'DT_CADASTRO': dt_cadastro,
                'NM_USUARIO': nm_usuario
            })

            print("Variado: " + str(id_counter))
            id_counter += 1
 
print(f'Dados gravados em {output_file}')
