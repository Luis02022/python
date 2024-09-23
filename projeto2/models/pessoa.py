
class Pessoa:
    def __init__(self, idade: int, nome: str) -> None:
        self.id = idade        
        self.nome = nome        
          

    def __str__(self) -> str:
        return  (f"\nIdade: {self.idade}"
                f"\nNome: {self.nome}")
              