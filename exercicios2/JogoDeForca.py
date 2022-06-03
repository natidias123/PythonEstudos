"""
O código pergunta uma palavra, dá chances e pergunta letras
o objetivo é acertar as letras da palavra
"""
# Define a palavra secreta, o número de chances e cria a lista digitadas
secreto = input('Qual será a palavra secreta? ')
digitadas = []
chances = 3

while True:  # Loop infinito pede letras até ganhar ou perder

    if chances <= 0:  # Define quando perde
        print('Você perdeu! ')
        break
    else:
        letra = input('Digite uma letra: ')

        if len(letra) > 1:  # Confere se foi digitado apenas uma letra
            print('Dígite apenas uma letra.')
            continue

        digitadas.append(letra)  # Adiciona a letra digitada na lista

        if letra in secreto:
            print(f'A letra {letra} EXISTE na palavra secreta!')
        else:
            print(f'A letra {letra} NÂO EXISTE na palavra secreta!')
            digitadas.pop  # Se a letra não está na palavra ela é retirada da lista

        secreto_temp = ''  # A palavra que será mostrada á pessoa

        for letra_secreta in secreto:  # Define letra secreta como cada letra em secreto
            if letra_secreta in digitadas:
                secreto_temp += letra_secreta  # Adiciona a letra a palavra mostrada à pessoa
            else:
                secreto_temp += '*'  # Se letra secreta não está em digitadas será adicionado * no lugar

        if secreto_temp == secreto:  # Define se a pessoa venceu
            print(f'Você GANHOU!! A palavra secreta era {secreto}.')
            break
        else:
            print(f'A palavra secreta está assim {secreto_temp}.')

        if letra not in secreto:  # Tira uma chance se a letra foi errada
            chances -= 1
            print(f'Você ainda tem {chances} chances.')
            print('')
