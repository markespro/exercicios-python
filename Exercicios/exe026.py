frase = str(input('Digite um frase \n')).strip().upper()

print('A letra A parece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A pareceu na posição {}'.format(frase.find('A')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))



