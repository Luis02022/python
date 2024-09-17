from projeto_pytest.models.enum.sexo import Sexo


class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: str, telefone: str, email: str, sexo: Sexo) -> None:
        self.id = id        
        self.nome = nome        
        self.dataNascimento = dataNascimento        
        self.telefone = telefone        
        self.email = email        
        self.sexo = sexo        
       

    def __str__(self) -> str:
        return  (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nData de Nascimento: {self.dataNascimento}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nSexo: {self.sexo.value}"
                )