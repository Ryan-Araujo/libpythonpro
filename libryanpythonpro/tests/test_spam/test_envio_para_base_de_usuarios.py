from unittest.mock import Mock

import pytest

from libryanpythonpro.spam.enviador_de_email import Enviador
from libryanpythonpro.spam.main import EnviadorDeSpam
from libryanpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
         [
            Usuario(nome='Ryan', email='ryanaraujo01112001@gmail.com'),
            Usuario(nome='Luciano', email='ryanaraujo01112001@gmail.com')
         ],

         [
            Usuario(nome='Ryan', email='ryanaraujo01112001@gmail.com')
         ]
    ]

)

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ryanaraujo01112001@python.pro,br',
        'Curso Python Pro,',
        'Confira os módulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count



def test_parametros_de_spam(sessao):
    usuario=Usuario(nome='Ryan', email='ryanaraujo01112001@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@python.pro.br',
        'Curso Python Pro,',
        'Confira os módulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@python.pro.br',
        'ryanaraujo01112001@gmail.com',
        'Cursos Python Pro',
        'Confira os módulos fantasticos'
    )




