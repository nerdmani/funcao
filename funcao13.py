def calcular_raiz_quadrada(numero, precisao = 0.0001):
    raiz = numero/2
    while abs(numero  - raiz**2) > precisao:
        raiz = (raiz + numero/raiz)/2
    return raiz

numero = int(input("Me de um numero papai: "))
raiz = calcular_raiz_quadrada(numero)
print('A riz quadrada de', numero, 'é', raiz)

#abs usado para mostrar o valor abslouto de um numero
#exemplo abaixo

print(abs(-5))