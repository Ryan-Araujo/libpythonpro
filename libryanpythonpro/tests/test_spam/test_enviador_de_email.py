import pytest

from libryanpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['ryanaraujo01112001@gmail.com','foo@bar.com.br']
                         )
def test_remetente(destinatario):
    enviador=Enviador()

    resultado = enviador.enviar(
    destinatario,
    'ryanzinhociclonado@gmail.com',
    'Estudos pythonPro',
    'Primeira turma aberta.')

    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['ryanaraujo.com','']
                         )
def test_remetente(destinatario):
    enviador=Enviador()
    with pytest.raises(EmailInvalido):

        enviador.enviar(
        destinatario,
        'ryanzinhociclonado@gmail.com',
        'Estudos pythonPro',
        'Primeira turma aberta.'
        )

