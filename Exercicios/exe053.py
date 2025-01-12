frase = str(input('Escreva uma frase ')).strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# Sobre o Range
# Start: Foi utilizado o -1, porque os porque os índices em Python começam do zero.
# Stop: Colocamos -1 para garantir que o índice 0 seja incluído, pois o stop não é alcançado.
# Step:  -1 iterar de trás para frente

for letra in range(len(junto)-1,-1,-1): 
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
