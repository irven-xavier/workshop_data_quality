from app.funcao import funcao_ola

def teste_funcao_ola():
    saida = funcao_ola()
    gabarito = "ola"
    assert saida == gabarito