"""
cidade a tem população de 80000 habitantes com taxa anual de crescimento de 3%
cidade b tem população de 200000 habitantes com taxa anual de crescimento de 1.5%

O programa conta quantos anos são necessários para cidade a ter mais habitantes que cidade b
"""

pop_a = 80000
pop_b = 200000
anos = 0

while pop_a < pop_b:
    aumento_a = pop_a * 0.03
    pop_a = pop_a + aumento_a
    aumento_b = pop_b * 0.015
    pop_b = pop_b + aumento_b
    anos = anos + 1

print(f'Em {anos} anos a população da cidade a é igual a {pop_a:.2f} e da cidade b é {pop_b:.2f}')
    