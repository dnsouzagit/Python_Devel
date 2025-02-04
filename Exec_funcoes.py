"""
# Exemplo 02

def soma (num1, num2):

    return num1+num2


val1=int(input('digite o primeiro número para somar: '))
val2=int(input('digite o segundo número para somar: '))

print(f'\nO Valor da Soma é: {soma(val1, val2)}')

# exemplo 02

def soma (*par):
    return sum(par)


num = []
val=''
while val!='s':
    num.append(float(input(f'\nDigite um número para somar: ')))
    print(f'\nA soma dos números {num} é: {soma(*num)}')
    print(f'\nA quantidade de numeros digitados são {len(num)}')
    val=input(f'Digite "s" para sair ou qualquer técla para continuar: ')
    if val == "s":
        break


# Exercício 01

def dobro(par):
    return (par*2)

num=int(input('\ndigite um inteiro para calcular seu dobro: '))
print(f'\nO dobro do número digitado é: {dobro(num)}')

# Exercício 03

def ValMaximo(*arg):
    return max(arg)

lista=[]
i=''
while i != 's':
    lista.append(int(input(f'\nDigite um número para coloca na lista: ')))
    print(f'\nA lista digitada é: {lista}')

    i=input(f'\nDigite (s) para sair, (max) para saber o valor máximo, ou enter para continuar a lista: ')
    
    if i=='max':
         print(f'\no valor máximo da lista digitada é: {ValMaximo(*lista)}')
    elif i=='s':
        break
       

"""

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista2 = [x+1 for x in lista]

print(lista2)
       

