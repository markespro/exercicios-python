soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulheres_20anos = 0
for pessoas in range(1,4):
    print('----{}ª PESSOA----'.format(pessoas))
    nome = str(input('Nome ')).strip()
    idade = int(input('Idade '))
    sexo = str(input('Sexo [M/F] ')).strip()
    soma_idade = soma_idade + idade
    if pessoas ==1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres_20anos += 1
media_idade = soma_idade/4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O mais homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho.capitalize()))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulheres_20anos))
 