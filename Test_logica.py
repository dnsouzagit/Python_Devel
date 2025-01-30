def horaseg(hora_cru):
    Hora_lista = [int(x) for x in hora_cru.split(":")]
    return (Hora_lista[0]*3600 + Hora_lista[1]*60 + Hora_lista[2])

entrada = input("digite o valor da hora no formato HH:MM:SS para converter em segundos: ")
print(f'\nO Valor de {entrada} em segundo é: {horaseg(entrada)}')