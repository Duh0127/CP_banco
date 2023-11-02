
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
    
with open(output_file2, 'w', newline='', encoding='utf-8') as csvfile2:
        fieldnames2 = ['ID_FUNC', 'NR_CNH',
                    'NM_CATEGORIA_CNH',
                    'DT_VALIDADE_CNH',
                    'DT_CADASTRO',
                    'NM_USUARIO']
        writer2 = csv.DictWriter(csvfile2, fieldnames=fieldnames2)
 
        writer2.writeheader()
    
        fake = Faker('pt_BR')

    
        for _ in range(1500000):
            nr_cnh = f"{random.randint(10000000, 99999999)}"
            nm_categoria_cnh = random.choice(["B", "C", "D", "E"])
            dt_validade_cnh = fake.date_between_dates(datetime(1980, 1, 1), datetime(2023, 12, 31)).strftime('%Y-%m-%d').upper()
            dt_cadastro = datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
            nm_usuario = "RM552164"
            

            writer2.writerow({
                
                    'ID_FUNC':id_counter,
                    'NR_CNH':nr_cnh,
                    'NM_CATEGORIA_CNH':nm_categoria_cnh,
                    'DT_VALIDADE_CNH':dt_validade_cnh,
                    'DT_CADASTRO': dt_cadastro,
                    'NM_USUARIO': nm_usuario
            })


            print("Motorista: " + str(id_counter))
            id_counter += 1

    