'''
Há uma escala que determina em quais dias da semana quais veículos não podem
circular. Essa escala é regida pelo último dígito da placa do veículo, sendo:
---------------------------------------------------------------------------------------
*Segunda-feira, digito final da placa 1 e 2
*Terça-feira, digito final da placa 3 e 4
*Quarta-feira, digito final da placa 5 e 6
*Quinta-feira, digito final da placa 7 e 8
*Sexta-feira, digito final da placa 9 e 0

O formato esperado para uma placa veicular válida em São Paulo é "AAA-9999",
tal que A é um caracter válido em [A-Z], e 9 um dígito numérico válido em [0-9]
'''

t = int(input())
placas = []
for placa in range(t):
    p = list(input().split("-"))
    placas.append(p)
for checar in placas:
    if (len(checar) == 1 or len(checar[0]) != 3 or len(checar[1]) != 4
        or checar[0].isupper() == False or checar[1].isdigit() == False
            or checar[0].isalpha() == False):
        print("FAILURE")
    else:
        if (checar[1][-1] == "2" or checar[1][-1] == "1"):
            print("MONDAY")
        elif (checar[1][-1] == "3" or checar[1][-1] == "4"):
            print("TUESDAY")
        elif (checar[1][-1] == "5" or checar[1][-1] == "6"):
            print("WEDNESDAY")
        elif (checar[1][-1] == "7" or checar[1][-1] == "8"):
            print("THURSDAY")
        elif (checar[1][-1] == "9" or checar[1][-1] == "0"):
            print("FRIDAY")
