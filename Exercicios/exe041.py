from datetime import date
 
ano_nascimento = int(input('Digite o seu ano de nascimento'))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Categoria MIRIM')
elif 9 < idade <= 14:
    print('Categoria INFANTIL')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade <= 20:
    print('Categoria SÊNIOR ')
elif 20 < idade:
    print('Categoria MASTER')





