"""
Código que calcula o salário de uma pessoa
com base na quantidade de horas trabalhadas e no valor/hora recebido
e desconta IR, INSS e sindicato
"""
# Recebe o valor recebido por hora
valor = input('Quanto você ganha por hora? ')

# Verifica se o número digitado pode ser convertido em inteiro
if not valor.isnumeric():
    print('Você deve digitar apenas o valor')

# Converte o valor para inteiro, recebe quantas horas são trabalhadas por mês e verifica se pode ser convertido em inteiro
else:
    valor = int(valor)
    horas = input('Quantas horas você tranalha por mês? ')
    if not horas.isnumeric():
        print('Você deve digitar apenas a quantidade de horas')

    # Converte a quantidade de horas mensais em inteiro e calcula o salario
    else:
        horas = int(horas)
        salario = valor * horas

    # Calcula os devidos valores descontados do salário
    ir = salario * 0.11
    inss = salario * 0.08
    sindicato = salario * 0.05
    salario_liq = salario - ir - inss - sindicato
    print()
    print(f'O seu salário bruto corresponde a {salario} reais,')
    print(f'o valor pago de IR {ir} reais, de INSS {inss} reais,')
    print(
        f'de sindicato {sindicato} reais e o salário líquido é de {salario_liq}')
