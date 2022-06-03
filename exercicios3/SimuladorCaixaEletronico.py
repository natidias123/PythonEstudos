"""
Esse código funciona como um caixa eletrônico
a pessoa diz quanto quer sacar e o caixa informa quais notas ela receberá
"""
# Recebe qual o valor que será sacado e verifica se pode ser convertido para inteiro
valor = input('Qual será o valor do saque? ')
if not valor.isnumeric():
    print('O valor digitado deve ser apenas um número inteiro.')

# Converte o valor para inteiro e calcula quantas notas serão retiradas para esse valor
else:
    valor = int(valor)
    nota100 = valor // 100
    valortemp = valor % 100
    nota50 = valortemp // 50
    valortemp = valortemp % 50
    nota10 = valortemp // 10
    valortemp = valortemp % 10
    nota5 = valortemp // 5
    valortemp = valortemp % 5
    nota1 = valortemp // 1
    valortemp = valortemp % 1
    print(
        f'Serão sacadas {nota100} notas de 100, {nota50} de 50, {nota10} de 10, {nota5} de 5 e {nota1} de 1 para {valor} reais')
