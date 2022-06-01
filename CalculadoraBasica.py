"""
Uma calculadora que resolve contas de +, -, * e / com números float
"""

while True:
    print()
    sair = input('Você deseja sair? (s ou n) ')

    if sair == 's':
        break

    else:
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')

        if not num1.replace('.', '', 1).isdigit and num2.replace('.', '', 1).isdigit:
            print('Você deve digitar apenas números')

        else:
            operador = input('Qual operação deve ser realizada? (+, -, *, /) ')

            if operador == '+':
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
