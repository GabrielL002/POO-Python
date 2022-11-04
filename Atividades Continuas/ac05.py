arquivo = open("notas.txt", "r", encoding='UTF-8')
aprovados = open('aprovados.txt', 'w', encoding='UTF-8')
reprovados = open('reprovados.txt', 'w', encoding='UTF-8')

apr = []
repr = []
for linha in arquivo:
    acs = []
    prova = 0
    sub = 0
    faltas = 0
    aluno = linha.split(";")
    prova = float(aluno[7])
    sub = float(aluno[8])
    faltas = float(aluno[9])
    for i in range(2, 7):
        acs.append(float(aluno[i]))
    if sub > prova:
        sub, prova = prova, sub
    acs.sort(reverse=True)
    acs.pop()
    media = ((sum(acs)/len(acs) + prova)/2)
    if (media >= 6.0 and faltas <= 20):
        apr.append(aluno[1])
    else:
        repr.append(aluno[1])
apr.sort()
repr.sort()
for a in apr:
    aprovados.write(f"{a}\n")

for a in repr:
    reprovados.write(f"{a}\n")


arquivo.close()
aprovados.close()
reprovados.close()
