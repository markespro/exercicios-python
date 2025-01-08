n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
if n1 > n2:
    print('O \033[1;33m primeiro valor é  MAIOR\033[m')
elif n1 < n2:
    print('O \033[1;33m Segundo valor é MAIOR \033[m ')
else: 
    print('\033[1;31m Os dois valores SÃO IGUAIS \033[m, os dois são iguais')


