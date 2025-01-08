from datetime import datetime

ano_nascimento = int(input('Digite o seu ano de nascimento'))
ano_atual = datetime.now()
idade = ano_atual.year - ano_nascimento

print('Quem nasceu em {} e tem {} anos em {}'.format(ano_nascimento, idade, ano_atual.year))

if idade < 18:
    print('\033[0;31mAinda faltam {} anos para o alistamento\033[m'.format(18-idade))
elif idade == 18:
    print('\033[0;31mVocê tem que se alistar imediatamente\033[m')
elif idade > 18:
    print('\033[0;31mVocê deveria ter se alistado há {} anos \033[m'.format(idade))
    print('Seu alistamento foi em {} anos'.format(idade-18))
