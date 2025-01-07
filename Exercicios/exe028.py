from random import randint
from time import sleep

bot = randint(0,5) # faz o computador "PENSAR"
player = int(input('Estou pensando em número de 0 a 5, tente adivinhar?\n')) # Jogador tenta adivinhar
print('Processando...')
sleep(2)

if player == bot:
    print('Você ACERTOU, eu pensei em {}'.format(player,bot))
else:
    print('Você ERROU, eu pensei em {}'.format(bot))