casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salário atual?'))
anos = int(input('Com quantos anos você deseja pagar o seu emprestimo?'))

parcelas = casa/(anos * 12)
limite = salario*0.30

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa,anos))
print('a prestação será de R${:.2f}'.format(parcelas))

if parcelas <= limite:
    print('\033[1;32mEmprestimo aprovado\033[m, sua parcela será de R${:.2f}'.format(parcelas))
else:
    print('\033[1;31mEmprestimo Negado\033[m')