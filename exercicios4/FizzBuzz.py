"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da
função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível
por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""
def fb(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        return 'FizzBuzz'
    if num1 % 3 == 0 and num1 % 5 > 0:
        return 'Fizz'
    if num1 % 3 > 0 and num1 % 5 == 0:
        return 'Buzz'
    return num1

num1 = int(input('Digite um número: '))

print(fb(num1))
