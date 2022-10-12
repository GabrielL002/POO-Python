'''
O navegador de Lucas possui um campo de busca onde o usuário poderá inserir uma palavra chave, e ao clicar em um botão de confirmação, 
ele será redirecionado para outra página com os resultados de sua pesquisa. Quando alguma string for digitada no campo de busca, Lucas 
quer que seu programa exiba, logo abaixo, algumas opções para auto completar esta string de acordo com as buscas já realizadas pelo usuário.

 Por exemplo, se as palavras “algoritmos” e “algas” já foram pesquisadas, ao digitar a string “alg”, o programa deverá sugerir as palavras
“algoritmos” e “algas”. Portanto, para cada string digitada, o programa deverá sugerir palavras pesquisadas anteriormente e que possuem como 
prefixo esta string. Caso alguma palavra seja igual a string digitada, ela também deve ser sugerida.
'''

t = int(input())
p = []
for _ in range(0, t):
    v = input()
    p.append(v)
z = int(input())
Q = []
for busca in range(0, z):
    v = input()
    Q.append(v)
for char in Q:
    i = 0
    buscas = 0
    maiorP = ""
    nAchado = []
    while i < t:
        k = 0
        plvIgual = True
        for busca in char:
            if (busca != p[i][k]):
                plvIgual = False
                break
            k += 1
        if (plvIgual):
            buscas += 1
            if (len(maiorP) < len(p[i])):
                maiorP = p[i]

        i += 1
    if (buscas == 0):
        print(-1)
    else:
        print(f"{buscas} {len(maiorP)}")
