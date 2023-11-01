from datetime import datetime
import random
from faker import Faker
import oracledb

fake = Faker('pt_BR')
conn = oracledb.connect(user="rm551763", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

id_counter = 5001

cpf_set = set()
rg_set = set()

data_minima = datetime(1900, 1, 1)
data_maxima = datetime.now()

sql = """INSERT INTO T_RHSTU_PACIENTE 
             (ID_PACIENTE, NM_PACIENTE, NR_CPF, NM_RG, DT_NASCIMENTO, FL_SEXO_BIOLOGICO, DS_ESCOLARIDADE, DS_ESTADO_CIVIL, NM_GRUPO_SANGUINEO, NR_ALTURA, NR_PESO, DT_CADASTRO, NM_USUARIO) 
             VALUES 
             (:ID_PACIENTE, :NM_PACIENTE, :NR_CPF, :NM_RG, TO_DATE(:DT_NASCIMENTO, 'DD-MON-YYYY'), :FL_SEXO_BIOLOGICO, :DS_ESCOLARIDADE, :DS_ESTADO_CIVIL, :NM_GRUPO_SANGUINEO, :NR_ALTURA, :NR_PESO, SYSDATE, USER)"""

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

    conn.commit()
cur.close()
conn.close()
