from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range (1,4):
    ano_nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(pessoas)))
    idade = ano_atual - ano_nasc
    if idade >= 21: #MAIOR de idade
        total_maior += 1 #contador MENORES de idade   
    else:
        total_menor += 1 #contador MAIORES de idade
print('E também tivemos {} pessoas MENORES de idade'.format(total_menor))
print('E também tivemos {} pessoas MAIORES de idade'.format(total_maior))