# ARQUIVO DE TESTE
# Este é um programa de teste para a Atividade Continua 01.
# Este arquivo não deve ser alterado.


from ac01 import posicoes, remover_itens_repetidos, media_notas, excluir_menor_nota, caracter_mais_frequente


print('--------------------------------------------------------------')
try:
    tupla = (1, 2, 3, 4, 5)
    resultado = posicoes(tupla, 2)
    assert resultado == [1]
    print('posicoes - CORRETO')
except AssertionError:
    print('posicoes - ERRADO')

try:
    tupla = (2, 1, 2, 3, 2, 2, 9, 2)
    resultado = posicoes(tupla, 2)
    assert resultado == [0, 2, 4, 5, 7]
    print('posicoes - CORRETO')
except AssertionError:
    print('posicoes - ERRADO')

try:
    tupla = (2, 1, 2, 3, 2)
    resultado = posicoes(tupla, 5)
    assert resultado == []
    print('posicoes - CORRETO')
except AssertionError:
    print('posicoes - ERRADO')


print('--------------------------------------------------------------')
try:
    lista = [2, 1, 2, 3, 2, 2, 9, 2, 4, 5, 6, 6, 10, 9, 1, 1]
    resultado = remover_itens_repetidos(lista)
    assert resultado == [1, 2, 3, 4, 5, 6, 9, 10]
    print('remover_itens_repetidos - CORRETO')
except AssertionError:
    print('remover_itens_repetidos - ERRADO')

try:
    lista = [5, 5, 5, 5, 5]
    resultado = remover_itens_repetidos(lista)
    assert resultado == [5]
    print('remover_itens_repetidos - CORRETO')
except AssertionError:
    print('remover_itens_repetidos - ERRADO')

try:
    lista = [9, 8, 7, 6, 5, 4, 3]
    resultado = remover_itens_repetidos(lista)
    assert resultado == [3, 4, 5, 6, 7, 8, 9]
    print('remover_itens_repetidos - CORRETO')
except AssertionError:
    print('remover_itens_repetidos - ERRADO')


print('--------------------------------------------------------------')
try:
    alunos = {'Augusto': [4.0, 7.0, 6.0, 3.0],
              'Denise': [9.0, 9.0, 9.0],
              'Ana Paula': [3.5, 9.5, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = media_notas(alunos)
    assert resultado == {'Augusto': 5.0,
                         'Denise': 9.0,
                         'Ana Paula': 6.5,
                         'Marcelo': 8.25}
    print('media_notas - CORRETO')
except AssertionError:
    print('media_notas - ERRADO')

try:
    alunos = {'Augusto': [9.0],
              'Denise': [6.0, 7.0],
              'Ana Paula': [9.0, 9.0, 9.0, 9.0]}
    resultado = media_notas(alunos)
    assert resultado == {'Augusto': 9.0,
                         'Denise': 6.5,
                         'Ana Paula': 9.0}
    print('media_notas - CORRETO')
except AssertionError:
    print('media_notas - ERRADO')

try:
    alunos = {'Augusto': [9.0],
              'Denise': [6.0],
              'Ana Paula': [5.5]}
    resultado = media_notas(alunos)
    assert resultado == {'Augusto': 9.0,
                         'Denise': 6.0,
                         'Ana Paula': 5.5}
    print('media_notas - CORRETO')
except AssertionError:
    print('media_notas - ERRADO')


print('--------------------------------------------------------------')
try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = excluir_menor_nota(alunos, 'Denise')
    assert resultado == {'Augusto': [4.5, 7.0, 6.0, 3.0],
                         'Denise': [9.0],
                         'Ana Paula': [3.5, 1.0, 6.5],
                         'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    print('excluir_menor_nota - CORRETO')
except AssertionError:
    print('excluir_menor_nota - ERRADO')

try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = excluir_menor_nota(alunos, 'Marcelo')
    assert resultado == {'Augusto': [4.5, 7.0, 6.0, 3.0],
                         'Denise': [9.0, 8.5],
                         'Ana Paula': [3.5, 1.0, 6.5],
                         'Marcelo': [9.0, 10.0, 7.0]}
    print('excluir_menor_nota - CORRETO')
except AssertionError:
    print('excluir_menor_nota - ERRADO')

try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = excluir_menor_nota(alunos, 'Fernando')
    assert resultado == {'Augusto': [4.5, 7.0, 6.0, 3.0],
                         'Denise': [9.0, 8.5],
                         'Ana Paula': [3.5, 1.0, 6.5],
                         'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    print('excluir_menor_nota - CORRETO')
except AssertionError:
    print('excluir_menor_nota - ERRADO')


print('--------------------------------------------------------------')
try:
    texto = 'faculdade de tecnologia impacta'
    resultado = caracter_mais_frequente(texto)
    assert resultado == 'a'
    print('caracter_mais_frequente - CORRETO')
except AssertionError:
    print('caracter_mais_frequente - ERRADO')

try:
    texto = 'exemplo de texto aleatorio para teste'
    resultado = caracter_mais_frequente(texto)
    assert resultado == 'e'
    print('caracter_mais_frequente - CORRETO')
except AssertionError:
    print('caracter_mais_frequente - ERRADO')

try:
    texto = 'existem muitas variacoes de textos disponiveis, mas a maior parte sofreu alteracoes de alguma forma'
    resultado = caracter_mais_frequente(texto)
    assert resultado == ' '                     # espaço em branco
    print('caracter_mais_frequente - CORRETO')
except AssertionError:
    print('caracter_mais_frequente - ERRADO')
