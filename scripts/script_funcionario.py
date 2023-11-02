
import random
import csv
from faker import Faker
from datetime import datetime
 
fake = Faker('pt_BR')
 
data_min = datetime(2022, 1, 1, 0, 0, 0)
data_max = datetime(2023, 12, 31, 23, 59, 59)
id_counter = 1
 
# Nome do arquivo CSV de saída
output_file = 'D:/dados_FUNCIONARIOS3.csv'
output_file2 = 'D:/dados_MOTORISTA.csv'
output_file3 = 'D:/dados_MED.csv'
 
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID_FUNC', 'ID_SUPERIOR', 'NM_FUNC', 'DS_CARGO', 'DT_NASCIMENTO', 'VL_SALARIO', 'NR_RG', 'NR_CPF', 'ST_FUNC', 'DT_CADASTRO', 'NM_USUARIO']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
 
    fake = Faker('pt_BR')




    # Criar 8.000 registros com o cargo de "Médico"
    for _ in range(3000000):
        if id_counter > 1:
            id_superior = random.randint(1, id_counter - 1)  # ID superior aleatório
        else:
            id_superior = None
        nm_func = fake.name()  # Nome do funcionário
        ds_cargo = "Médico"
        dt_nascimento = fake.date_between_dates(data_min, data_max).strftime('%Y-%m-%d').upper()
        vl_salario = random.randint(8000, 15000)  # Valor aleatório entre 8000 e 15000
        nr_rg = fake.random_int(min=1000000, max=9999999)  # Número de RG de 7 dígitos
        nr_cpf = fake.random_int(min=10000000000, max=99999999999)  # Número de CPF de 11 dígitos
        st_func = random.choice(['A', 'I'])  # Status aleatório (Ativo ou Inativo)
        dt_cadastro = datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
        nm_usuario = "RM552164"
        
            
        writer.writerow({
                'ID_FUNC':id_counter,
                'ID_SUPERIOR':id_superior,
                'NM_FUNC':nm_func,
                'DS_CARGO':ds_cargo,
                'DT_NASCIMENTO':dt_nascimento,
                'VL_SALARIO':vl_salario,
                'NR_RG':nr_rg,
                'NR_CPF':nr_cpf,
                'ST_FUNC':st_func,
                'DT_CADASTRO': dt_cadastro,
                'NM_USUARIO': nm_usuario

        })
        
        print("Médico: " + str(id_counter))
            
    
        print(id_counter)
        id_counter += 1
        # Criar 3.000 registros com o cargo de "Motorista"

    for _ in range(1500000):
        id_superior = random.randint(1, id_counter - 1)  # ID superior aleatório
        nm_func = fake.name()  # Nome do funcionário
        ds_cargo = "Motorista"
        dt_nascimento = fake.date_between_dates(data_min, data_max).strftime('%Y-%m-%d').upper()
        vl_salario = random.randint(2500, 4000)  # Valor aleatório entre 2500 e 4000
        nr_rg = fake.random_int(min=1000000, max=9999999)  # Número de RG de 7 dígitos
        nr_cpf = fake.random_int(min=10000000000, max=99999999999)  # Número de CPF de 11 dígitos
        st_func = random.choice(['A', 'I'])  # Status aleatório (Ativo ou Inativo)
        dt_cadastro = datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
        nm_usuario = "RM552164"
        
        
        writer.writerow({
                'ID_FUNC':id_counter,
                'ID_SUPERIOR':id_superior,
                'NM_FUNC':nm_func,
                'DS_CARGO':ds_cargo,
                'DT_NASCIMENTO':dt_nascimento,
                'VL_SALARIO':vl_salario,
                'NR_RG':nr_rg,
                'NR_CPF':nr_cpf,
                'ST_FUNC':st_func,
                'DT_CADASTRO': dt_cadastro,
                'NM_USUARIO': nm_usuario

        })
        print("Motorista: " + str(id_counter))
        id_counter += 1

    # Criar 50.000 registros com cargos variados
    cargos_variados = ["Enfermeiro", "Cirurgião", "Recepcionista", "Residente", "Anestesista"]
    for _ in range(1500000):
        id_superior = random.randint(1, id_counter - 1)  # ID superior aleatório
        nm_func = fake.name()  # Nome do funcionário
        ds_cargo = random.choice(cargos_variados)
        dt_nascimento = fake.date_between_dates(data_min, data_max).strftime('%Y-%m-%d').upper()
        vl_salario = random.randint(2000, 8000)  # Valor aleatório entre 2000 e 8000
        nr_rg = fake.random_int(min=1000000, max=9999999)  # Número de RG de 7 dígitos
        nr_cpf = fake.random_int(min=10000000000, max=99999999999)  # Número de CPF de 11 dígitos
        st_func = random.choice(['A', 'I'])  # Status aleatório (Ativo ou Inativo)
        dt_cadastro = datetime.now().strftime('%Y-%m-%d:%H:%M:%S')
        nm_usuario = "RM552164"
        
        
        writer.writerow({
                'ID_FUNC':id_counter,
                'ID_SUPERIOR':id_superior,
                'NM_FUNC':nm_func,
                'DS_CARGO':ds_cargo,
                'DT_NASCIMENTO':dt_nascimento,
                'VL_SALARIO':vl_salario,
                'NR_RG':nr_rg,
                'NR_CPF':nr_cpf,
                'ST_FUNC':st_func,
                'DT_CADASTRO': dt_cadastro,
                'NM_USUARIO': nm_usuario

        })
        print("Variado: " + str(id_counter))
        id_counter += 1

    