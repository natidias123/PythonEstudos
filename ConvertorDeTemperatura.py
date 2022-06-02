"""
Código que converte a temperatura de célsius para fahrenheit ou vice versa
"""
# Recebe a informação de qual medida deverá ser calculada
medida = input('Qual medida será convertida? (c) ou (f) ')

# verifica se foi digitado apenas caracteres
if not medida.isalpha:
    print('Deve ser digitado apenas c para celsius ou f para fahrenheit')

# Reconhece se foi pedido celsius, pede a temperatura e realiza a conversão
elif medida == 'c':
    graus = input('Quantos graus celsius estão agora? ')

    if not graus.isnumeric:
        print('Deve ser utilizado apenas números para temperatura')

    else:
        graus = int(graus)
        f = graus * 1.8 + 32
        print(f'{graus} graus celsius é igual a {f} graus fahrenheit')

# Reconhece se foi fahrenheit, pede a temperatura e realiza a conversão
elif medida == 'f':
    graus = input('Quantos graus fahrenheit estão agora? ')

    if not graus.isnumeric:
        print('deve ser utilizado apenas números para temperatura')

    else:
        graus = int(graus)
        c = (graus - 32) / 1.8
        print(f'{graus} graus fahrenheit é igual a {c:.2f} graus celsius')

# Reconhece se não foi digitado apenas c ou f
else:
    print('deve ser utilizado apenas c para celsius ou f para fahrenheit')
