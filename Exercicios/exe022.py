nome_completo = str(input('Qual é o seu nome completo?')).strip()
divide = nome_completo.split()

print('Analisando seu nome...')
print('Seu nome completo em maiusculo é {}, '.format(nome_completo.upper()))
print('Seu nome com lestras minusculas é, {}'.format(nome_completo.lower()))
print('Seu nome contém ao todo {} letras'.format(len(nome_completo) - nome_completo.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(divide[0],len(divide[0])))

## print('O seu primeiro nome contem {} letras'.format(nome_completo.find(' ')))
