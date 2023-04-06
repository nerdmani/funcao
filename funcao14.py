#palindromo - palavra usada ou frase que se pode ler indiferente da esquerda da direita, ou vice-versa

def verif_palidromo(texto):
    texto = texto.lower().replace(' ','-' )
    texto = texto.lower().replace('^',',' )
    texto = texto.lower().replace('','-' )
    return texto == texto[::-1]
    
# texto [::-1] inverte o texto

texto = 'socorram-me, subi no ônibus em Marrocos'
if verif_palidromo(texto):
    print(texto, 'É um palindromo.')
else:
    print(texto, 'não é um palindromo.')