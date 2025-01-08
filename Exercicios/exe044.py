print('{:=^40}'.format(' MERCADINHO DOIS IRMAOS'))
preço = float(input('Preço de Compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão 
      [ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço *0.1)
elif opção == 2:
    total = preço - (preço *0.05)
elif opção == 3:
    total = preço
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f} no final.'.format(parcela))
elif opção == 4:
    total = preço + (preço *0.2)
    total_parcela = int(input('Quantas parcelas?'))
    parcela = total/ total_parcela
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(total_parcela, parcela))
else:
    total = 0
    print('\033[1;31mOPÇÃO INVÁLIDA DE PAGAMENTO, tente novamente!\033[m')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço,total))