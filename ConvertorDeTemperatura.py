"""
Código que converte a temperatura de célsius para fahrenheit ou vice versa
"""
medida = input('Qual medida será convertida? (c) ou (f) ')

if not medida.isalpha:
    print('Deve ser digitado apenas c para celsius ou f para fahrenheit')

elif medida == 'c':
    graus = input('Quantos graus celsius estão agora? ')

    if not graus.isnumeric:
        print('Deve ser utilizado apenas números para temperatura')

    else:
        graus = int(graus)
        f = graus * 1.8 + 32
        print(f'{graus} graus celsius é igual a {f} graus fahrenheit')

elif medida == 'f':
    graus = input('Quantos graus fahrenheit estão agora? ')

    if not graus.isnumeric:
        print('deve ser utilizado apenas números para temperatura')

    else:
        graus = int(graus)
        c = (graus - 32) / 1.8
        print(f'{graus} graus fahrenheit é igual a {c:.2f} graus celsius')

else:
    print('deve ser utilizado apenas c para celsius ou f para fahrenheit')
