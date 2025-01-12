numero = int(input('Encontre o número primo'))
total = 0
for c in range(1,numero + 1):
    if numero % c ==0: #Verificando se é primo
        print('\033[33m', end='')
        total = total+1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mo número {} foi divivísel {} vezes'.format(numero,total))
if total ==2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
