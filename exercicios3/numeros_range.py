"""
programa que imprima na tela os números de 1 a 20, um abaixo do outro
depois modifique o programa para que ele mostre os números um ao lado do outro
"""

for n in range(1, 21):
    print(n)

for n in range(1, 21):
    print(n, end='')
    print(', ' if n < 20 else '.', end='')
print()

"""
Programa que imprime na tela apenas os números ímpares entre 1 e 50
"""
for n in range(1, 51, 2):
    print(n, end='')
    print(', ' if n < 49 else '.', end='')
print()

"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.
"""
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
soma = 0

if num2.isnumeric() and num1.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        for n in range(num2+1, num1):
            print(n, end='')
            print(', ' if n < num1-1 else '.', end='')
            soma += n
    else:
        for n in range(num1+1, num2):
            print(n, end='')
            print(' ' if n < num2-1 else '.', end='')
            soma += n
    print()
    print(f'A soma dos números entre {num1} e {num2} é igual a {soma}')
else:
    print('Deve ser digitado apenas um número inteiro.')
