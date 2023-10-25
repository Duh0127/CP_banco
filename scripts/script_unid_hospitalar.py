from datetime import datetime
import random
from faker import Faker
import oracledb

fake = Faker('pt_BR')

conn = oracledb.connect(user="rm552164", password="fiap23", dsn="oracle.fiap.com.br/orcl")
cur = conn.cursor()

data_min = datetime(1950, 1, 1)
data_max = datetime(2023, 10, 17)

# Contador para ID da unidade hospitalar
id_counter = 1

# Quantidade de unidades hospitalares a serem criadas
for _ in range(20000):
    nm_unid_hospitalar = fake.first_name() + fake.last_name() + " Hospital"
    nm_razao_social = fake.company()  # Gere nomes de empresas fictícias
    # Garanta que dt_fundacao seja menor que dt_inicio
    while True:
        dt_fundacao = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
        dt_inicio = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
        if datetime.strptime(dt_fundacao, '%d-%b-%Y') < datetime.strptime(dt_inicio, '%d-%b-%Y'):
            break
    nr_logradouro = int(random.randint(1, 20000))
    if random.choice([True, False]):
        while True:
            dt_termino = fake.date_between_dates(data_min, data_max).strftime('%d-%b-%Y').upper()
            if datetime.strptime(dt_termino, '%d-%b-%Y') >= datetime.strptime(dt_inicio, '%d-%b-%Y'):
                break
    else:
        dt_termino = None
    
    cur.execute(
        """INSERT INTO T_RHSTU_UNID_HOSPITALAR (ID_UNID_HOSPITAL, NM_UNID_HOSPITALAR, NM_RAZAO_SOCIAL_UNID_HOSP, DT_FUNDACAO, NR_LOGRADOURO, DS_COMPLEMENTO_NUMERO, DS_PONTO_REFERENCIA, DT_INICIO, DT_TERMINO, DT_CADASTRO, NM_USUARIO)
           VALUES
           (:ID_UNID_HOSPITAL, :NM_UNID_HOSPITALAR, :NM_RAZAO_SOCIAL_UNID_HOSP, TO_DATE(:DT_FUNDACAO, 'DD-MM-YYYY'), :NR_LOGRADOURO, :DS_COMPLEMENTO_NUMERO, :DS_PONTO_REFERENCIA, TO_DATE(:DT_INICIO, 'DD-MM-YYYY'), :DT_TERMINO, SYSDATE, USER)""",
        ID_UNID_HOSPITAL=id_counter,
        NM_UNID_HOSPITALAR=nm_unid_hospitalar,
        NM_RAZAO_SOCIAL_UNID_HOSP=nm_razao_social,
        DT_FUNDACAO=dt_fundacao,
        NR_LOGRADOURO=nr_logradouro,
        DS_COMPLEMENTO_NUMERO=None,
        DS_PONTO_REFERENCIA=None,
        DT_INICIO=dt_inicio,
        DT_TERMINO=dt_termino,
    )
    id_counter += 1
    print(id_counter)

conn.commit()
cur.close()
conn.close()
