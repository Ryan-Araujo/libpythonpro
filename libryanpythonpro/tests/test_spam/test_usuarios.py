from libryanpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Ryan', email='ryanaraujo01112001@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = \
        [
        Usuario(nome='Ryan', email='ryanaraujo01112001@gmail.com'),
        Usuario(nome='Luciano', email='ryanaraujo01112001@gmail.com')
        ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()


