"""
Uma calculadora que resolve contas de +, -, * e / com números float
"""

num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

# confere se os números digitados podem ser convertidos em float
if not num1.replace('.', '', 1).isdigit and num2.replace('.', '', 1).isdigit:
    print('Você deve digitar apenas números')

else:
    operador = input('Qual operação deve ser realizada? (+, -, *, /) ')

    if operador == '+':
        # reconhece o operador, converte os números em float e realiza a operação
        resultado = float(num1) + float(num2)
        print(resultado)

    elif operador == '-':
        resultado = float(num1) - float(num2)
        print(resultado)

    elif operador == '*':
        resultado = float(num1) * float(num2)
        print(resultado)

    elif operador == '/':
        resultado = float(num1) / float(num2)
        print(resultado)

    else:
        print('O operador deve ser apenas +, -, * ou /')
