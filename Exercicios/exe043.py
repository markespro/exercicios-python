peso = float(input('Digite o seu peso atual (em Kg)'))
altura = float(input('Digite a sua altura em (Metros)'))

imc = peso/(altura **2)

if imc < 18.5:
    print('\033[0;31mAbaixo do peso [PALITO]\033[m seu IMC é {:.1f}'.format(imc))
elif  18.5 <= imc < 25:
    print('\033[0;31mPeso Ideal [NA MEDIDA]\033[m seu IMC é {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('\033[0;31mSobrepeso [ROLIÇO]\033[m, seu IMC é {:.1f}'.format(imc))
elif 30 < imc <= 40:
    print('\033[0;31mObesidade [GORDO]\033[m seu IMC é {:.1f}'.format(imc))
elif 40 < imc:
    print('\033[0;31mObesidade mórbida [GORDAO]\033[m seu IMC é {:.1f}'.format(imc))