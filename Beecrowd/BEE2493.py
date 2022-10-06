'''
JOGO DOS OPERADORES
Samu Elmito adora criar jogos peculiares para desafiar seus amigos. Desta vez, ele inventou um jogo chamado
"Jogo do Operador", em que ele cria expressões básicas e cada jogador deve escolher uma expressão e preencher
a lacuna com o operador correto para validá-la. Os jogadores poderão escolher operadores de somente
três tipos: adição, subtração e multiplicação. Porém, se o jogador achar que não há operador entre os três tipos 
que valide a expressão, poderá responder Impossível.

Sua tarefa é simples: dadas as expressões e as respostas dos jogadores, determinar os jogadores que
não passarão para a outra fase do jogo
EXEMPLO DE ENTRADA:                  EXEMPLO DE SAÍDA:
3                                    Aline Samuel
8 4=5
2 5=5
1 3=4
Samuel 2 +
Abner 3 +
Aline 1 *
'''
while True:
    try:
        acertos = []
        erros = []
        xyz = []
        ner = []
        t = int(input())          
        for i in range(0, t): 
            v, z = input().split("=")
            v1, v2 = v.split()
            v1 = int(v1)
            v2 = int(v2)
            z = int(z)
            valores = [v1, v2, z]
            xyz.append(valores)
        for i in range(0, t):
            p, alt, o = input().split()
            alt = int(alt)
            player = [p, alt, o]
            ner.append(player)
        for i in range(0, t):
            x = xyz[ner[i][1]-1][0]
            y = xyz[ner[i][1]-1][1]
            z = xyz[ner[i][1]-1][2]
            if (ner[i][2] == "+"):
                if (x + y == z):
                    acertos.append(ner[i][0])
                else:
                    erros.append(ner[i][0])
            elif (ner[i][2] == "-"):
                if (x - y == z):
                    acertos.append(ner[i][0])
                else:
                    erros.append(ner[i][0])
            elif (ner[i][2] == "I"):
                if (x + y != z and x - y != z and x * y != z):
                    acertos.append(ner[i][0])
                else:
                    erros.append(ner[i][0])
            else:
                if (x * y == z):
                    acertos.append(ner[i][0])
                else:
                    erros.append(ner[i][0])

        if (len(erros) == t):
            print("None Shall Pass!")
        elif (len(acertos) == t):
            print("You Shall All Pass!")
        else:
            erros.sort()
            for i in erros:
                if (i == erros[-1]):
                    print(i, end='')
                else:
                    print(i, end=" ")
            print()

    except EOFError:
        break
