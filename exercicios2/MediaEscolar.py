"""
O programa pede tres notas parciais de um aluno, pergunta a média, 
calcula a média e responde se o aluno foi aprovado, reprovado 
ou aprovado com distinção (se a média for igual a 10).
"""
# Recebe as notas e confere se podem ser convertidas em float. E recebe a média e confere se pode ser convertido para inteiro
nota1 = input('Digite a nota 1: ')
if not nota1.replace('.', '', 1).isdigit():
    print('Deve ser digitado apenas a nota.')

nota2 = input('Digite a nota 2: ')
if not nota2.replace('.', '', 1).isdigit():
    print('Deve ser digitado apenas a nota.')

nota3 = input('Digite a nota 3: ')
if not nota3.replace('.', '', 1).isdigit():
    print('Deve ser digitado apenas a nota.')

media = input('Qual é a média para aprovação? ')
if not media.isnumeric():
    print('Deve ser digitado apenas numeros na média.')

# Converte a média para inteiro, as notas para float e calcula a média
media = int(media)
nota_media = (float(nota1) + float(nota2) + float(nota3)) / 3

# Reconhece se foi reprovado, aprovado ou aprovado com distinção
if nota_media < media:
    print(f'Você foi REPROVADO, sua média é de {nota_media:.2f}.')

elif nota_media >= media and nota_media < 10:
    print(f'Você foi APROVADO, sua média é de {nota_media:.2f}.')

elif nota_media == 10:
    print('Você foi APROVADO COM DISTINÇÃO, tirou 10!')
