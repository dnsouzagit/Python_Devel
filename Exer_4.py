'''
Exercício 1

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

if num1>num2:
    print(f"O maior número digitado é: {num1}")
else:
    print(f"O maior número digitado é: {num2}")

Exercício 2

import math

num = int(input('Digite o número: '))

if num>=0:
    print(f"A ráiz quadrade de {num} é: {math.sqrt(num)}")
else:
    print(f" o número {num} é inválido!")

Exercício 3

num = int(input('Digite o número: '))

result =  bool(num % 2)

if result:
    print(f'O número {num} é impar!')
else:
    print(f'O número {num} é par!')




'''


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

if num1>num2:
    print(f"\nO maior número digitado é: {num1}\n")
elif num1 == num2:
    print(f"\nO número {num1} é igual ao número {num2}\n")
else:
    print(f"\nO maior número digitado é: {num2}\n")

