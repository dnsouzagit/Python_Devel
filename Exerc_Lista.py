lista = []
num: int
sair =''

while True:
    num=int(input('\nadicione um numero a sua lista: '))
    lista.append(num)
    lista.sort()
    print(f'\n {lista}')
    sair=input('\ndigite s para sair ou enter para continuar adcionando itens a lista:')
    if sair=='s':
        break

lista2=(list(range(20)))
print(lista2)
lista2 += lista
print(lista2)
print('fim')



