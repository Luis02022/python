import os 

os.system("cls || clear")

class Livro:
    def __init__(self, titulo: str, autor: str, numero_paginas: int, preco: float) -> None:
        self.titulo = titulo 
        self.autor = autor 
        self.numero_paginas = numero_paginas
        self.preco = preco

    def exibir_dados_livro(self) -> str:
        return f"\nTítulo: {self.titulo} \nAutor: {self.autor} \nNúmero de páginas: {self.numero_paginas} \nPreço: R${self.preco}"    
    


livro = Livro("O Mendingo", "Marmota", 100, 150.62) 
livro2 = Livro("AKAKAKAK", "TiqueTique", 89, 500.65
               )
print(livro.exibir_dados_livro())
print(livro2.exibir_dados_livro())