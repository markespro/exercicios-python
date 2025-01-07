sal = float(input('Qaul é o seu salário?'))

aum10 = 0.1*sal
aum15 = 0.15*sal

if sal <= 1250.00:
    print('Seu aumento foi de R$ {:.2f} Seu novo salário é de R${:.2f}'.format(aum15,(aum15+sal)))
else:
    print('Seu aumento foi de R$ {:.2F} Seu novo salário é de R${:.2f}'.format(aum10,(aum10+sal)))


