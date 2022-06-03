"""
Código que calcula o imc de uma pessoa com base nos dados perguntados
conferindo se os dados recebidos estão no formato correto, se não, avisa
"""
peso = input('qual o seu peso? ')

if not peso.isnumeric:
    print('Deve ser digitado apenas números para o peso')

else:
    peso = int(peso)
    altura = input('qual sua altura? ')

    if not altura.replace('.', '', 1).isdigit:
        print('Deve ser utilizado apenas numeros no formato 0.00 para altura')

    else:
        altura = float(altura)
        imc = peso / (altura * 2)
        print(f'O seu IMC é igual a {imc:.2f}')
