'''
A letra 'a' é representada por um único ponto '.'
A letra 'b' é representada por dois pontos '..'
A letra 'c' é representada por três pontos '...'
As demais letras seguem a lógica anterior, porém cada conjunto de pontos está
separado por um espaço e sempre com um conjunto a mais de pontos, como no
exemplo abaixo:
. → a
.. → b
... → c
. . → d
.. .. → e
... ... → f
. . . → g
.. .. .. → h
... ... ... → i
'''
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while True:
    try:
        t = int(input())
        for i in range(0, t):
            n = list(input().split())
            if (n[0] == "..."):
                letra = 3*len(n)
                print(abc[letra-1])
            elif (n[0] == ".."):
                letra = 2*len(n) + len(n)-1
                print(abc[letra-1])
            else:
                x = len(n)
                if (x == 1):
                    letra = 1
                elif (x == 2):
                    letra = 4
                elif (x == 3):
                    letra = 7
                elif (x == 4):
                    letra = 10
                elif (x == 5):
                    letra = 13
                elif (x == 6):
                    letra = 16
                elif (x == 7):
                    letra = 19
                elif (x == 8):
                    letra = 22
                elif (x == 9):
                    letra = 25
                print(abc[letra-1])
    except EOFError:
        break
