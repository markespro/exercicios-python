
n1 = float(input('Primeira nota'))
n2 = float(input('Segunda nota?'))

med = (n1 + n2) / 2
print('Tirando {} e {} a sua média foi de {}'.format(n1,n2,med))

if med < 5:
    print('\033[1;31mO aluno foi REPROVADO\033[m,')
elif 5 <= med <= 6.9:
    print('\033[1;33mO aluno vai para RECUPERAÇÃO\033[m')
elif med >= 7:
    print('\033[1;32mO aluno foi APROVADO\033[m')



