from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Sua opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[1;34mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('\033[1;34mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCE\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('\033[\033[1;32mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[1;34mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')
else:
    print('Digite uma opção válida')