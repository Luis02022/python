import os 

# os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero

#    def exibir_endereco(self) -> str:
 #       return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
        


class Aluno:
    #nome, idade
    #Construtor 
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        #Atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


    #def exibir_dados(self) -> str:
        #return f"Aluno:\nNome:  {self.nome} \nIdade: {self.idade}  \n\nEndereço: {self.endereco.exibir_endereco()}"

    def __str__(self) -> str:
        return f"Aluno:\nNome:  {self.nome} \nIdade: {self.idade}  \n\nEndereço: {self.endereco}"
        

#Instanciar classe:
#endereco = Endereco("Bonfim", 40)
#aluno = Aluno("Marta", 56, endereco)

aluno = Aluno("Marta", 22, Endereco("Rua A", 10))


print(aluno)
#print(aluno.exibir_dados())
#print(endereco.exibir_endereco())