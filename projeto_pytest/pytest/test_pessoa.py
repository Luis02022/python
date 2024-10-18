import pytest
from projeto_pytest.models.pessoa import Pessoa
from ..models.enum.sexo import Sexo 

@pytest.fixture
def criar_pessoa():
    # pessoa1= Pessoa(5454, "Rafael", "11/07/2001", "7194002711", "rafael.senai.gmaiç.com", Sexo.MASCULINO)
    return Pessoa(5454, "Rafael", "11/07/2001", "7194002711", "rafael.senai.gmaiç.com", Sexo.MASCULINO)

def test_nome(criar_pessoa):
    assert criar_pessoa.nome == "Rafael"

