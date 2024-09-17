from models.enum.sexo import Sexo# Primeira Forma
from models.endereco import Endereco
from models.pessoa import Pessoa #Caminho Relativo
from models.enum.unidadefederativa import UnidadeFederativa #Caminho Absoluto
import os 


pessoa1 = Pessoa(1515, "Luis", "04/11/1985", "71 40028922", "luisin@gmail.com", Sexo.MASCULINO,
                 Endereco("Rua A", "50", "Prédio", "41525222", "Salvador", UnidadeFederativa.BAHIA))

print(pessoa1)

