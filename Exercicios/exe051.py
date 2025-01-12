
print('='*25)
print('\033[0;31m10 TERMOS DE UMA PA\033[m')
print('='*25)
termo = int(input('Primeiro Termo'))
razao = int(input('Razao'))

for c in range(1,11):
    pa = termo + (c-1)*razao
    print('{} '.format(pa), end=' -> ')
print('ACABOU')