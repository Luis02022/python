from models.pessoa import Pessoa
import pytest

@pytest 
def pessoa_valida(Pessoa):
    pessoa = Pessoa(18, "Marta")
    return pessoa

def test_pessoa_alterar_nome_valido(pessoa_valida):
    #Alterando o nome da pessoa de "Marta" para "Vitoria"
    pessoa_valida.nome = "Vitoria"
    assert pessoa_valida.nome == "Vitoria"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Marta"


def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida == 18

def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):    
    with pytest.raises(ValueError, match = "Idade não pode ser negativa"):
        Pessoa(-1, "Marta")