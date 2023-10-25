from datetime import datetime
import random
from faker import Faker
import oracledb

fake = Faker('pt_BR')

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

# Data mínima e máxima para datas de nascimento
data_min = datetime(1900, 1, 1)
data_max = datetime(2005, 12, 31)

# Contador para ID de funcionário
id_counter = 1

# Criar 8.000 registros com o cargo de "Médico"
for _ in range(8000):
    if id_counter > 1:
        id_superior = random.randint(1, id_counter - 1)  # ID superior aleatório
    else:
        id_superior = None
    nm_func = fake.name()  # Nome do funcionário
    ds_cargo = "Médico"
    dt_nascimento = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
    vl_salario = random.uniform(8000, 15000)  # Valor aleatório entre 8000 e 15000
    nr_rg = fake.random_int(min=1000000, max=9999999)  # Número de RG de 7 dígitos
    nr_cpf = fake.random_int(min=10000000000, max=99999999999)  # Número de CPF de 11 dígitos
    st_func = random.choice(['A', 'I'])  # Status aleatório (Ativo ou Inativo)
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"
    
    cur.execute(
        """INSERT INTO T_RHSTU_FUNCIONARIO (ID_FUNC, ID_SUPERIOR, NM_FUNC, DS_CARGO, DT_NASCIMENTO, VL_SALARIO, NR_RG, NR_CPF, ST_FUNC, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_FUNC, :ID_SUPERIOR, :NM_FUNC, :DS_CARGO, TO_DATE(:DT_NASCIMENTO, 'DD-MON-YYYY'), :VL_SALARIO, :NR_RG, :NR_CPF, :ST_FUNC, SYSDATE, USER)""",
        ID_FUNC=id_counter,
        ID_SUPERIOR=id_superior,
        NM_FUNC=nm_func,
        DS_CARGO=ds_cargo,
        DT_NASCIMENTO=dt_nascimento,
        VL_SALARIO=vl_salario,
        NR_RG=nr_rg,
        NR_CPF=nr_cpf,
        ST_FUNC=st_func
    )
    print("Médico: " + str(id_counter))
    id_counter += 1

# Criar 3.000 registros com o cargo de "Motorista"
for _ in range(3000):
    id_superior = random.randint(1, id_counter - 1)  # ID superior aleatório
    nm_func = fake.name()  # Nome do funcionário
    ds_cargo = "Motorista"
    dt_nascimento = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
    vl_salario = random.uniform(2500, 4000)  # Valor aleatório entre 2500 e 4000
    nr_rg = fake.random_int(min=1000000, max=9999999)  # Número de RG de 7 dígitos
    nr_cpf = fake.random_int(min=10000000000, max=99999999999)  # Número de CPF de 11 dígitos
    st_func = random.choice(['A', 'I'])  # Status aleatório (Ativo ou Inativo)
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"
    
    cur.execute(
        """INSERT INTO T_RHSTU_FUNCIONARIO (ID_FUNC, ID_SUPERIOR, NM_FUNC, DS_CARGO, DT_NASCIMENTO, VL_SALARIO, NR_RG, NR_CPF, ST_FUNC, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_FUNC, :ID_SUPERIOR, :NM_FUNC, :DS_CARGO, TO_DATE(:DT_NASCIMENTO, 'DD-MON-YYYY'), :VL_SALARIO, :NR_RG, :NR_CPF, :ST_FUNC, SYSDATE, USER)""",
        ID_FUNC=id_counter,
        ID_SUPERIOR=id_superior,
        NM_FUNC=nm_func,
        DS_CARGO=ds_cargo,
        DT_NASCIMENTO=dt_nascimento,
        VL_SALARIO=vl_salario,
        NR_RG=nr_rg,
        NR_CPF=nr_cpf,
        ST_FUNC=st_func
    )
    print("Motorista: " + str(id_counter))
    id_counter += 1

# Criar 50.000 registros com cargos variados
cargos_variados = ["Enfermeiro", "Cirurgião", "Recepcionista", "Residente", "Anestesista"]
for _ in range(50000):
    id_superior = random.randint(1, id_counter - 1)  # ID superior aleatório
    nm_func = fake.name()  # Nome do funcionário
    ds_cargo = random.choice(cargos_variados)
    dt_nascimento = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
    vl_salario = random.uniform(2000, 8000)  # Valor aleatório entre 2000 e 8000
    nr_rg = fake.random_int(min=1000000, max=9999999)  # Número de RG de 7 dígitos
    nr_cpf = fake.random_int(min=10000000000, max=99999999999)  # Número de CPF de 11 dígitos
    st_func = random.choice(['A', 'I'])  # Status aleatório (Ativo ou Inativo)
    dt_cadastro = "SYSDATE"
    nm_usuario = "USER"
    
    cur.execute(
        """INSERT INTO T_RHSTU_FUNCIONARIO (ID_FUNC, ID_SUPERIOR, NM_FUNC, DS_CARGO, DT_NASCIMENTO, VL_SALARIO, NR_RG, NR_CPF, ST_FUNC, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_FUNC, :ID_SUPERIOR, :NM_FUNC, :DS_CARGO, TO_DATE(:DT_NASCIMENTO, 'DD-MON-YYYY'), :VL_SALARIO, :NR_RG, :NR_CPF, :ST_FUNC, SYSDATE, USER)""",
        ID_FUNC=id_counter,
        ID_SUPERIOR=id_superior,
        NM_FUNC=nm_func,
        DS_CARGO=ds_cargo,
        DT_NASCIMENTO=dt_nascimento,
        VL_SALARIO=vl_salario,
        NR_RG=nr_rg,
        NR_CPF=nr_cpf,
        ST_FUNC=st_func
    )
    print("Variado: " + str(id_counter))
    id_counter += 1

conn.commit()
cur.close()
conn.close()
