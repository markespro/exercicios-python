sum = 0
cont = 0
for number in range(1,501,2):
    if number % 3 == 0:
        cont = cont +1
        sum = sum + number
print('A soma de todos os {} valores solicita é {}'.format(cont,sum))
