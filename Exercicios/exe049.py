number = int(input('Digite um número para ver sua tabuada: '))
for cont in range(1,11):
    print('{} x {:2} = {} '.format(number,cont,(number*cont)))