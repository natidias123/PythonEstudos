"""
Simulador de caixa de mercado que recebe pagamento em dinheiro

Recebe um número de valores indeterminado, depois será informado o total da compra
então deve-se informar em quantidade de notas e moedas o valor do pagamento
por fim, será checado se o pagamento foi suficiente e quanto será o troco

# obs
quando terminar de informar os valores dos itens digite fim para sair do loop
"""

#lista vazia em que serão registrado os valores dos produtos
produtos = []

#loop infinito que registra o valor dos produtos, para sair deve digitar 'fim'
while True:

    prod1 = input('fim para sair. Digite o valor do item: ')
    if prod1 == 'fim':
        break

    if not prod1.replace('.', '', 1).isdigit():
        print('Deve ser digitado o valor no formato 00.00')
        continue
    else:
        prod1 = float(prod1)

    produtos.append(prod1)
    prod1 = 0

#lista quantos produtos tem e os respectivos valores
num = 1
print('---------------------')
for n in produtos:
    print(f'Produto {num} - R$ {n:.2f}')
    num += 1 

#informa o valor total 
total = sum(produtos)
print()
print(f'Total - R$ {total:.2f}')
print()

#recebe as notas e moedas para pagamento e verifica quando o pagamento é suficiente saindo do laço 
notas100 = int(input('Quantas notas de 100 serão usadas para o pagamento? '))
pagamento = notas100 * 100
if not pagamento >= total:
    notas50 = int(input('Quantas notas de 50 serão usadas para o pagamento? '))
    pagamento = pagamento + (notas50 * 50)
    if not pagamento >= total:
        notas20 = int(input('Quantas notas de 20 serão usadas para o pagamento? '))
        pagamento = pagamento + (notas20 * 20)
        if not pagamento >= total:
            notas10 = int(input('Quantas notas de 10 serão usadas para o pagamento? '))
            pagamento = pagamento + (notas10 * 10)
            if not pagamento >= total:
                notas5 = int(input('Quantas notas de 5 serão usadas para o pagamento? '))
                pagamento = pagamento + (notas5 * 5)
                if not pagamento >= total:
                    notas2 = int(input('Quantas notas de 2 serão usadas para o pagamento? '))
                    pagamento = pagamento + (notas2 * 2)
                    if not pagamento >= total:
                        moeda1 = int(input('Quantas moedas de 1 real serão usadas para o pagamento? '))
                        pagamento = pagamento + (moeda1 * 1)
                        if not pagamento >= total:
                            moeda50 = float(input('Quantas moedas de 50 centavos serão usadas para o pagamento? '))
                            pagamento = pagamento + (moeda50 * 0.5)
                            if not pagamento >= total:
                                moeda25 = float(input('Quantas moedas de 25 centavos serão usadas para o pagamento? '))
                                pagamento = pagamento + (moeda25 * 0.25)
                                if not pagamento >= total:
                                    moeda10 = float(input('Quantas moedas de 10 centavos serão usadas para o pagamento? '))
                                    pagamento = pagamento + (moeda10 * 0.10)
                                    if not pagamento >= total:
                                        moeda5 = float(input('Quantas moedas de 5 centavos serão usadas para o pagamento? '))
                                        pagamento = pagamento + (moeda5 * 0.5)
                                        if not pagamento >= total:
                                            moeda1c = float(input('Quantas moedas de 1 centavo serão usadas para o pagamento? '))
                                            pagamento = pagamento + (moeda1c * 0.01)

#informa se o pagamento foi suficiente ou insuficiente e informa o troco a receber
if pagamento == total:
    print()
    print(f'O pagamento em dineiro foi de {pagamento} reais e não terá troco')
elif pagamento < total:
    print()
    print(f'O pagamento de {pagamento} reais foi insuficiente e faltou {total - pagamento:.2f} reais de pagamento')
else:
    print()
    print(f'O pagamento em dinheiro foi de {pagamento} reais e o troco será de {pagamento-total:.2f} reais')
