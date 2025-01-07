dis = float(input('Qua a distância da sua viagem em km?'))

if dis >= 200:
    print('Sua passagem custa R${:.2f}'.format(dis*0.45))
else:
    print('Sua passagem custa R${:.2f}'.format(dis*0.5))


