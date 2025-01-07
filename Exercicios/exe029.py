vel = float(input('Qual é a velocidade atual do carro?'))

multa = (vel- 80)*7
#aplicando condição simples
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('A multa vai custar R${:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')