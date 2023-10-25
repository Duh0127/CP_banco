from datetime import datetime
import random
from faker import Faker
import oracledb

fake = Faker('pt_BR')

# Configurações de conexão com o banco de dados Oracle
conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

# Contador para gerar IDs únicos
id_counter = 5001

# Set para garantir a unicidade dos CPFs e RGs
cpf_set = set()
rg_set = set()

# Data mínima e máxima para data de nascimento
data_minima = datetime(1900, 1, 1)
data_maxima = datetime.now()

sql = """INSERT INTO T_RHSTU_PACIENTE 
             (ID_PACIENTE, NM_PACIENTE, NR_CPF, NM_RG, DT_NASCIMENTO, FL_SEXO_BIOLOGICO, DS_ESCOLARIDADE, DS_ESTADO_CIVIL, NM_GRUPO_SANGUINEO, NR_ALTURA, NR_PESO, DT_CADASTRO, NM_USUARIO) 
             VALUES 
             (:ID_PACIENTE, :NM_PACIENTE, :NR_CPF, :NM_RG, TO_DATE(:DT_NASCIMENTO, 'DD-MON-YYYY'), :FL_SEXO_BIOLOGICO, :DS_ESCOLARIDADE, :DS_ESTADO_CIVIL, :NM_GRUPO_SANGUINEO, :NR_ALTURA, :NR_PESO, SYSDATE, USER)"""


# Quantidade de objetos criados
for _ in range(1000):
    id = id_counter
    id_counter += 1

    nome = fake.name()

    while True:
        cpf = fake.unique.random_int(min=100000000, max=999999999)
        if cpf not in cpf_set:
            cpf_set.add(cpf)
            break

    while True:
        rg = fake.unique.random_int(min=10000000, max=99999999)
        if rg not in rg_set:
            rg_set.add(rg)
            break

    nasc = fake.date_between_dates(data_minima, data_maxima).strftime('%d-%b-%Y').upper()
    sexo = random.choice(["M", "F", "I"])
    escolaridade = fake.random_element(
        elements=(
            "ENSINO FUNDAMENTAL",
            "ENSINO MÉDIO",
            "ENSINO SUPERIOR",
            "PÓS-GRADUAÇÃO",
            "MESTRADO",
            "DOUTORADO",
            "PÓS-DOUTORADO",
            "PHD",
        )
    )
    status_civil = fake.random_element(
        elements=(
            "SOLTEIRO",
            "CASADO",
            "DIVORCIADO",
            "VIÚVO",
            "SEPARADO",
            "UNIÃO ESTÁVEL",
        )
    )
    tipo_sanguineo = fake.random_element(elements=("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"))
    altura = random.uniform(0.5, 2.3)
    peso = random.uniform(5, 500)

    print("Id: ", id)

    cur.execute(
        sql,
        ID_PACIENTE=id,
        NM_PACIENTE=nome,
        NR_CPF=str(cpf),
        NM_RG=str(rg),
        DT_NASCIMENTO=nasc,
        FL_SEXO_BIOLOGICO=sexo,
        DS_ESCOLARIDADE=escolaridade,
        DS_ESTADO_CIVIL=status_civil,
        NM_GRUPO_SANGUINEO=tipo_sanguineo,
        NR_ALTURA=altura,
        NR_PESO=peso,
    )



    # # DIVISÃO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    # id2 = id_counter
    # id_counter += 1
    # nome2 = fake.name()

    # while True:
    #     cpf2 = fake.unique.random_int(min=100000000, max=999999999)
    #     if cpf2 not in cpf_set:
    #         cpf_set.add(cpf2)
    #         break

    # while True:
    #     rg2 = fake.unique.random_int(min=10000000, max=99999999)
    #     if rg2 not in rg_set:
    #         rg_set.add(rg2)
    #         break

    # nasc2 = fake.date_between_dates(data_minima, data_maxima).strftime('%d-%b-%Y').upper()
    # sexo2 = random.choice(["M", "F", "I"])
    # escolaridade2 = fake.random_element(
    #     elements=(
    #         "ENSINO FUNDAMENTAL",
    #         "ENSINO MÉDIO",
    #         "ENSINO SUPERIOR",
    #         "PÓS-GRADUAÇÃO",
    #         "MESTRADO",
    #         "DOUTORADO",
    #         "PÓS-DOUTORADO",
    #         "PHD",
    #     )
    # )
    # status_civil2 = fake.random_element(
    #     elements=(
    #         "SOLTEIRO",
    #         "CASADO",
    #         "DIVORCIADO",
    #         "VIÚVO",
    #         "SEPARADO",
    #         "UNIÃO ESTÁVEL",
    #     )
    # )
    
    # tipo_sanguineo2 = fake.random_element(elements=("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"))
    # altura2 = random.uniform(0.5, 2.3)
    # peso2 = random.uniform(5, 500)

    # cur.execute(
    #     sql,
    #     ID_PACIENTE=id2,
    #     NM_PACIENTE=nome2,
    #     NR_CPF=str(cpf2),
    #     NM_RG=str(rg2),
    #     DT_NASCIMENTO=nasc2,
    #     FL_SEXO_BIOLOGICO=sexo2,
    #     DS_ESCOLARIDADE=escolaridade2,
    #     DS_ESTADO_CIVIL=status_civil2,
    #     NM_GRUPO_SANGUINEO=tipo_sanguineo2,
    #     NR_ALTURA=altura2,
    #     NR_PESO=peso2,
    # )


    # # DIVISÃO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    # id3 = id_counter
    # id_counter += 1
    # nome3 = fake.name()

    # while True:
    #     cpf3 = fake.unique.random_int(min=100000000, max=999999999)
    #     if cpf3 not in cpf_set:
    #         cpf_set.add(cpf3)
    #         break

    # while True:
    #     rg3 = fake.unique.random_int(min=10000000, max=99999999)
    #     if rg3 not in rg_set:
    #         rg_set.add(rg3)
    #         break

    # nasc3 = fake.date_between_dates(data_minima, data_maxima).strftime('%d-%b-%Y').upper()
    # sexo3 = random.choice(["M", "F", "I"])
    # escolaridade3 = fake.random_element(
    #     elements=(
    #         "ENSINO FUNDAMENTAL",
    #         "ENSINO MÉDIO",
    #         "ENSINO SUPERIOR",
    #         "PÓS-GRADUAÇÃO",
    #         "MESTRADO",
    #         "DOUTORADO",
    #         "PÓS-DOUTORADO",
    #         "PHD",
    #     )
    # )
    # status_civil3 = fake.random_element(
    #     elements=(
    #         "SOLTEIRO",
    #         "CASADO",
    #         "DIVORCIADO",
    #         "VIÚVO",
    #         "SEPARADO",
    #         "UNIÃO ESTÁVEL",
    #     )
    # )
    
    # tipo_sanguineo3 = fake.random_element(
    #     elements=("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-")
    # )
    # altura3 = random.uniform(0.5, 2.3)
    # peso3 = random.uniform(5, 500)

    # cur.execute(
    #     sql,
    #     ID_PACIENTE=id3,
    #     NM_PACIENTE=nome3,
    #     NR_CPF=str(cpf3),
    #     NM_RG=str(rg3),
    #     DT_NASCIMENTO=nasc3,
    #     FL_SEXO_BIOLOGICO=sexo3,
    #     DS_ESCOLARIDADE=escolaridade3,
    #     DS_ESTADO_CIVIL=status_civil3,
    #     NM_GRUPO_SANGUINEO=tipo_sanguineo3,
    #     NR_ALTURA=altura3,
    #     NR_PESO=peso3,
    # )



    # # DIVISÃO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    # id4 = id_counter
    # id_counter += 1
    # nome4 = fake.name()

    # while True:
    #     cpf4 = fake.unique.random_int(min=100000000, max=999999999)
    #     if cpf4 not in cpf_set:
    #         cpf_set.add(cpf4)
    #         break

    # while True:
    #     rg4 = fake.unique.random_int(min=10000000, max=99999999)
    #     if rg4 not in rg_set:
    #         rg_set.add(rg4)
    #         break

    # nasc4 = fake.date_between_dates(data_minima, data_maxima).strftime('%d-%b-%Y').upper()
    # sexo4 = random.choice(["M", "F", "I"])
    # escolaridade4 = fake.random_element(
    #     elements=(
    #         "ENSINO FUNDAMENTAL",
    #         "ENSINO MÉDIO",
    #         "ENSINO SUPERIOR",
    #         "PÓS-GRADUAÇÃO",
    #         "MESTRADO",
    #         "DOUTORADO",
    #         "PÓS-DOUTORADO",
    #         "PHD",
    #     )
    # )
    # status_civil4 = fake.random_element(
    #     elements=(
    #         "SOLTEIRO",
    #         "CASADO",
    #         "DIVORCIADO",
    #         "VIÚVO",
    #         "SEPARADO",
    #         "UNIÃO ESTÁVEL",
    #     )
    # )
    
    # tipo_sanguineo4 = fake.random_element(elements=("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"))
    # altura4 = random.uniform(0.5, 2.3)
    # peso4 = random.uniform(5, 500)

    # cur.execute(
    #     sql,
    #     ID_PACIENTE=id4,
    #     NM_PACIENTE=nome4,
    #     NR_CPF=str(cpf4),
    #     NM_RG=str(rg4),
    #     DT_NASCIMENTO=nasc4,
    #     FL_SEXO_BIOLOGICO=sexo4,
    #     DS_ESCOLARIDADE=escolaridade4,
    #     DS_ESTADO_CIVIL=status_civil4,
    #     NM_GRUPO_SANGUINEO=tipo_sanguineo4,
    #     NR_ALTURA=altura4,
    #     NR_PESO=peso4,
    # )



    # # DIVISÃO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    # id5 = id_counter
    # id_counter += 1
    # nome5 = fake.name()

    # while True:
    #     cpf5 = fake.unique.random_int(min=100000000, max=999999999)
    #     if cpf5 not in cpf_set:
    #         cpf_set.add(cpf5)
    #         break

    # while True:
    #     rg5 = fake.unique.random_int(min=10000000, max=99999999)
    #     if rg5 not in rg_set:
    #         rg_set.add(rg5)
    #         break

    # nasc5 = fake.date_between_dates(data_minima, data_maxima).strftime('%d-%b-%Y').upper()
    # sexo5 = random.choice(["M", "F", "I"])
    # escolaridade5 = fake.random_element(
    #     elements=(
    #         "ENSINO FUNDAMENTAL",
    #         "ENSINO MÉDIO",
    #         "ENSINO SUPERIOR",
    #         "PÓS-GRADUAÇÃO",
    #         "MESTRADO",
    #         "DOUTORADO",
    #         "PÓS-DOUTORADO",
    #         "PHD",
    #     )
    # )
    # status_civil5 = fake.random_element(
    #     elements=(
    #         "SOLTEIRO",
    #         "CASADO",
    #         "DIVORCIADO",
    #         "VIÚVO",
    #         "SEPARADO",
    #         "UNIÃO ESTÁVEL",
    #     )
    # )
    
    # tipo_sanguineo5 = fake.random_element(elements=("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"))
    # altura5 = random.uniform(0.5, 2.3)
    # peso5 = random.uniform(5, 500)

    # cur.execute(
    #     sql,
    #     ID_PACIENTE=id5,
    #     NM_PACIENTE=nome5,
    #     NR_CPF=str(cpf5),
    #     NM_RG=str(rg5),
    #     DT_NASCIMENTO=nasc5,
    #     FL_SEXO_BIOLOGICO=sexo5,
    #     DS_ESCOLARIDADE=escolaridade5,
    #     DS_ESTADO_CIVIL=status_civil5,
    #     NM_GRUPO_SANGUINEO=tipo_sanguineo5,
    #     NR_ALTURA=altura5,
    #     NR_PESO=peso5,
    # )

    conn.commit()

# Commit e fechamento de conexões
cur.close()
conn.close()
