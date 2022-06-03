"""
O programa pedirá 5 números e informará algumas coisas
"""
# Recebe os números e verifica se podem ser convertidos em float, se não puder, avisa
num1 = input('Digite o número 1: ')
if not num1.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número')

num2 = input('Digite o número 2: ')
if not num2.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número')

num3 = input('Digite o número 3: ')
if not num3.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número')

num4 = input('Digite o número 4: ')
if not num4.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número')

num5 = input('Digite o número 5: ')
if not num5.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número')

# Converte os números em float
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)
num5 = float(num5)
print('')

# Verifica qual é o maior número
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

# Calcula a soma e a média dos números
soma = num1 + num2 + num3 + num4 + num5
media = (num1 + num2 + num3 + num4 + num5) / 5
print(f'A soma de todos os números é {soma:.2f} e a média é {media:.2f}')

# Define listas para classificar os números pares, ímpares e decimais
pares = []
impares = []
decimais = []

# Calcula se os números tem resto ao ser dividido por 2
num1temp = num1 % 2
num2temp = num2 % 2
num3temp = num3 % 2
num4temp = num4 % 2
num5temp = num5 % 2

# Separa em classificações de acordo com o resto, se = 1 é ímpar, se = 0 par e entre 0 e 1 decimais
if num1temp == 1:
    impares.append(num1)
elif num1temp == 0:
    pares.append(num1)
else:
    decimais.append(num1)

if num2temp == 1:
    impares.append(num2)
elif num2temp == 0:
    pares.append(num2)
else:
    decimais.append(num2)

if num3temp == 1:
    impares.append(num3)
elif num3temp == 0:
    pares.append(num3)
else:
    decimais.append(num3)

if num4temp == 1:
    impares.append(num4)
elif num4temp == 0:
    pares.append(num4)
else:
    decimais.append(num4)

if num5temp == 1:
    impares.append(num5)
elif num5temp == 0:
    pares.append(num5)
else:
    decimais.append(num5)

print(
    f'Os números pares são {pares}, os ímpares são {impares} e os decimais são {decimais}')
