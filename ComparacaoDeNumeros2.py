"""
O programa pedirá 5 números e informará algumas coisas
"""
while True:
    num1 = input('Digite o número 1: ')
    if not num1.isnumeric():
        print('Deve ser digitado apenas o número inteiro.')
        break
    num2 = input('Digite o número 2: ')
    if not num2.isnumeric():
        print('Deve ser digitado apenas o número inteiro.')
        break
    num3 = input('Digite o número 3: ')
    if not num3.isnumeric():
        print('Deve ser digitado apenas o número inteiro.')
        break
    num4 = input('Digite o número 4: ')
    if not num4.isnumeric():
        print('Deve ser digitado apenas o número inteiro.')
        break
    num5 = input('Digite o número 5: ')
    if not num5.isnumeric():
        print('Deve ser digitado apenas o número inteiro.')
        break

    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    num5 = int(num5)

    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        print(f'O maior número dígitado é o {num1}')
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        print(f'O maior número dígitado é o {num2}')
    elif num3 > num2 and num3 > num1 and num3 > num4 and num3 > num5:
        print(f'O maior número dígitado é o {num3}')
    elif num4 > num2 and num4 > num3 and num4 > num1 and num4 > num5:
        print(f'O maior número dígitado é o {num4}')
    else:
        print(f'O maior número dígitado é o {num5}')

    # informa qual dos números é o maior.

    soma = num1 + num2 + num3 + num4 + num5
    media = (num1 + num2 + num3 + num4 + num5) / 5
    print(f'A soma de todos os números é {soma} e a média é {media}')

    pares = []
    impares = []

    num1temp = num1 % 2
    num2temp = num2 % 2
    num3temp = num3 % 2
    num4temp = num4 % 2
    num5temp = num5 % 2

    if num1temp > 0:
        impares.append(num1)
    else:
        pares.append(num1)
    if num2temp > 0:
        impares.append(num2)
    else:
        pares.append(num2)
    if num3temp > 0:
        impares.append(num3)
    else:
        pares.append(num3)
    if not num4temp > 0:
        impares.append(num4)
    else:
        pares.append(num4)
    if not num5temp > 0:
        impares.append(num5)
    else:
        pares.append(num5)

    print(f'Os números pares são {pares} e os ímpares são {impares}')

    break
