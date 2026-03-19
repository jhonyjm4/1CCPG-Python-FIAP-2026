import math

num1 = 5
num2 = 2

print(type(num1), type (num2))

operação = num1 / num2
print(operação, type(operação))

num = 15
print()
print(num)

num = num + 2
print(num)

num /= 2
print(num)

print()
print(6 >= 6)

idade = 21
print(idade >= 21)

logado = True
print(logado, type(logado))

maior_idade = idade >=18
print(maior_idade, type(maior_idade))

nome1 = "Marcos"
nome2 = "marcos"

print(nome1.upper()== nome2.upper())

num = 17
raiz = math.sqrt(num)
print(f"A raiz de {num} é {raiz:.2f}")

import random

num_random = random.random()
print(num_random*10)

num_rand_int = random.randint(1,10)
print(num_rand_int)
