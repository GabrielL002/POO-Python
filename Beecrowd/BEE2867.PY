'''
Dados dois números inteiros, n e m, quantos dígitos tem nm ?
Exemplos:
2 e 10 - 210 = 1024 - 4 dígitos

3 e 9 - 39 = 19683 - 5 dígitos
'''
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    n = str(x**y)
    print(len(n))
