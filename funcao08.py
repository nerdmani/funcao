def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media
    
notas = [10.0, 10.0, 10.0, 10.0]
media = calcular_media(notas)
print('A média é: ', media)
