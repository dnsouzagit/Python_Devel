"""
#Exercicio 1

lista=[]

for val in range(6):
    lista.append(int(input(f'Digite o Valor inteiro {val+1}/6: ')))

print(f'\n {lista}')


#Exercicio 2

A=[1, 0, 5, -2, -5, 7]
soma1= A[0]+A[1]+A[5]
print(f'A soma dos indices 0, 1 e 5 é: {soma1}')
A[5]=100

for i in A:
    print(i)

"""
# Exercício 3

lista=[]
pares=[]

for val in range(10):
    lista.append(int(input(f'Digite um Número inteiro {val+1}/10: ')))

print(f'\nA lista digitada é: {lista}')

for num in lista:
    if (num % 2) ==0:
        pares.append(num)

if len(pares)>0:
    print(f'\nOs números pares da lista são: {pares}')
    print(f'\nO total de números pares são: {len(pares)}')
else:
    print(f'\nA lista não contem Números Pares.')








