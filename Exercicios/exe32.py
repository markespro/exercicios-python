from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 oara analisar o ano atual:'))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' {} é bissexto)'.format(ano))
else:
    print(' {} Não é bissexto '.format(ano))
