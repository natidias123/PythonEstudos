"""
O código faz a comparação de 3 números diferentes e informa algumas informações
como média, informa em ordem crescente
"""
# Recebe os números, confere se pode ser convertido em float, se não puder, avisa
num1 = input('Digite o primeiro número: ')
if not num1.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número.')

num2 = input('Digite o segundo número: ')
if not num2.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número')

num3 = input('Digite o terceiro número: ')
if not num3.replace('.', '', 1).isdigit():
    print('Deve ser digitado um número')

# Converte os números em float
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

# Calcula a média
media = (num1 + num2 + num3) / 3
print('')
print(f'A média de {num1:.2f}, {num2:.2f} e {num3:.2f} é {media:.2f}')

# Organiza em ordem crescente
lista = [num1, num2, num3]
print('Os números em ordem crescente:', sorted(lista))

# Verifica qual número é o maior
if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')

# Verifica qual o menor
if num1 < num2 and num1 < num3:
    print(f'O menor número é {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O menor número é {num2}')
else:
    print(f'O menor número é {num3}')
