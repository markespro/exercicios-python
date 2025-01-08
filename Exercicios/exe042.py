print('\033[7;40m ===Analisar de Triângulos===\033[m')
print('\033[1;30m__\033[m'*20)

r1 = float(input('\033[0;33m Primeiro Segmento \033[m'))
r2 = float(input('\033[0;33m Segundo Segmento \033[m'))
r3 = float(input('\033[0;33m Terceiro Segmento \033[m'))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('\033[1;30;42m Os segmentos acima PODEM FORMAR triângulo \033[m')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('\033[1;31m Os segmentos acima NÃO PODEM FORMAR triângulo! \033[m')

    
