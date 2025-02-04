''' 


#Exercício_01
# Converte um número em uma lista ordenada

num = input('digite um numero para converte em uma lista Ordenada: ')

lista = sorted([int(x) for x in num])
print(lista)
'''

# Exercício_02 
# recebe uma string no formato hora:minuto:segundo e converte o valor para segundos

def retseg(Hour_raw):
    lista = [int(x) for x in (Hour_raw.split(":"))]
    return (lista[0]*3600) + (lista[1]*60) + (lista[2])



hora = input('digite o valor da hora para converte em segundos: ')
print(f'\nO valor de {hora} em segundos é: {retseg(hora)}')
