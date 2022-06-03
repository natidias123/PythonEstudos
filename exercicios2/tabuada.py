"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada.
"""
numtab = input('Qual número você deseja ver a tabuada 1-10: ')
if numtab.isnumeric():
    numtab = int(numtab)
    for n in range(1, 11):
        print(numtab, ' X ', n, ' = ', numtab*n)
else:
    print('Deve ser digitado apenas o número inteiro.')

