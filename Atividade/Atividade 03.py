from abc import ABC, abstractmethod
import os 

os.system("cls || clear")

class Endereco: 
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCidade: {self.cidade}"    
        



class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final (self) -> float:
        pass    

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email} \nEndereço: {self.endereco}"
    


#Médico

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return 5000.0
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}"
        )
    

#Engenheiro

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)        
        self.crea = crea


    def salario_final(self) -> float:
        return 2000.0
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
        )
    
        
#Instancionando classes
print("Dados do Engenheiro")        
engenehiro1 = Engenheiro("Roberto", "71925652", "roberto@gmail.com", Endereco("Rua A", "40", "Bloco B", "454545", "Salvador"), "45454")
print(engenehiro1)


print("\nDados do Médico:")
medico1 = Medico("Marta", "40028922", "marta@gmail.com", Endereco("Rua C", "5", "Bloco E", "654454-55", "Imbui"), "454422")
print(medico1)