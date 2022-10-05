'''
Implemente a função 'posicoes' que recebe como argumentos de entrada uma
tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item):
    indices = []
    for i in range(len(tupla)):
        if (tupla[i] == item):
            indices.append(i)
    return indices


'''
Implemente a função 'remover_itens_repetidos' que recebe como argumento
de entrada uma lista e remove todos os itens repetidos dessa lista. A função
deve retornar uma nova lista sem itens repetidos e ordenada de forma crescente.
'''


def remover_itens_repetidos(lista):
    newLista = list(set(lista))
    return newLista


'''
Considere um dicionario onde a chave é o nome de um aluno e o valor uma lista
de notas. Implemente a função 'media_notas' que recebe como argumento de
entrada o dicionário e retorna outro dicionário contendo os nomes e as médias
aritméticas de cada aluno.
'''


def media_notas(alunos):
    medias = {}
    for aluno in alunos:
        medias[aluno] = sum(alunos[aluno]) / len(alunos[aluno])
    return medias


'''
Considere um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Implemente a função 'excluir_menor_nota' que recebe como argumentos
de entrada o dicionário e o nome de um aluno. A função deve excluir a menor
nota do aluno informado e retornar o dicionário com as alterações realizadas.
Se aluno não estiver no dicionário, deve retornar o dicionário sem alterações.
'''


def excluir_menor_nota(alunos, nome):
    if (nome in alunos):
        menor = alunos[nome][0]
        for i in alunos[nome]:
            if (menor > i):
                menor = i
        alunos[nome].remove(menor)
    return alunos


'''
Implemente a função 'caracter_mais_frequente' que recebe como argumento de
entrada uma string e retorna o caracter que aparece com mais frequência na
string. Procure utilizar um dicionário para facilitar a implementação.
'''


def caracter_mais_frequente(texto):
    caracter = {}
    chrMaisFrequente = ["a", 0]
    for chr in texto:
        if (chr in caracter):
            caracter[chr] += 1
        else:
            caracter[chr] = 1
    for letra in caracter:
        if (caracter[letra] > chrMaisFrequente[1]):
            chrMaisFrequente = [letra, caracter[letra]]
    return chrMaisFrequente[0]
