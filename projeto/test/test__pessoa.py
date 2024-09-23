import pytest
from projeto.models.pessoa import Pessoa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Marta", 23)
    return pessoa


def test_pessoa_altrar_nome_valido(pessoa_valida):
    # Alterando o nome da Pessoa de "MAria" para "Vitoria"
    pessoa_valida.nome = "Vitoria"
    assert pessoa_valida.nome == "Vitoria"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Marta"