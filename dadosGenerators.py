from faker import Faker
import os
import time
import random


class dadosGenerators():
    def __init__(self):
        self.faker = Faker()

    def generator(self) -> dict:
        Nome = self.faker.name()
        idade = self.faker.random_int(min=20, max=100)
        sexo   = self.faker.random_element(elements=("Masculino", "Feminino"))
        trabalha = self.faker.random_element(elements=("Sim", "Nao"))
        Endereco = self.faker.address()
        Cidade = self.faker.city()
        CEP = self.faker.postcode()
        Telefone = self.faker.phone_number()
        Email = self.faker.email()
        renda = self.faker.random_int(min=1500, max=10000)
        return {"Nome": Nome, "Endereco": Endereco, "Cidade": Cidade, "CEP": CEP, "Telefone": Telefone, "Email": Email , "Idade": idade, "Sexo": sexo, "Trabalha": trabalha}


fake = dadosGenerators()

base_diretory = os.getcwd()

try:
    with open(os.path.join(base_diretory,"dadosTestes.txt"), "w") as file:
        file.write("#######################Dados#######################\n")

        for i in range(10000):
            data = fake.generator()
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
        
        
        dia = time.strftime("%d")
        mes = time.strftime("%m")
        ano = time.strftime("%Y")
        horario = time.strftime("%H:%M:%S")
        file.write(f"Dados colhidos na Data: {dia}/{mes}/{ano}, horario: {horario}\n")
        file.write("#######################Dados#######################\n")
except Exception as e:
    print(e)
