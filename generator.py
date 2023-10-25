import random
from faker import Faker

fake = Faker()

# Lista para armazenar os objetos
pessoas = []

# Contador para gerar IDs únicos
id_counter = 1

# Set para garantir a unicidade dos CPFs e RGs
cpf_set = set()
rg_set = set()

# Criação dos 100 objetos
for _ in range(1000):
    id = id_counter
    id_counter += 1

    nome = fake.name()

    # Gere CPF e RG únicos
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

    nasc = (
        fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d-%b-%Y").upper()
    )
    sexo = random.choice(["M", "F", "I"])
    escolaridade = fake.random_element(
        elements=("ENSINO FUNDAMENTAL", "ENSINO MÉDIO", "ENSINO SUPERIOR", "PÓS-GRADUAÇÃO", "MESTRADO", "DOUTORADO", "PÓS-DOUTORADO", "PHD")
    )
    status_civil = fake.random_element(
        elements=("SOLTEIRO", "CASADO", "DIVORCIADO", "VIÚVO", "SEPARADO", "UNIÃO ESTÁVEL")
    )
    tipo_sanguineo = fake.random_element(
        elements=("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-")
    )
    altura = random.uniform(1.5, 2.2)
    peso = random.uniform(50, 120)

    # Defina data_atual e usuario_atual como valores fixos
    data_atual = "SYSDATE"
    usuario_atual = "USER"

    pessoa = {
        "id": id,
        "nome": nome,
        "cpf": str(cpf),
        "rg": str(rg),
        "nasc": nasc,
        "sexo": sexo,
        "escolaridade": escolaridade,
        "status_civil": status_civil,
        "tipo_sanguineo": tipo_sanguineo,
        "altura": altura,
        "peso": peso,
        "data_atual": data_atual,
        "usuario_atual": usuario_atual,
    }

    pessoas.append(pessoa)

# Verifique se há duplicatas
for campo in ["cpf", "rg"]:
    valores = [pessoa[campo] for pessoa in pessoas]
    if len(valores) != len(set(valores)):
        print(f"Duplicatas encontradas no campo {campo}")

# Exiba os 5 primeiros objetos como exemplo
for i in range(1000):
    print(pessoas[i])
