print('Digite o número de um ano e eu direi se é um ano bissexto')

ano = int(input('Digite o ano: '))

if ano%4==0 and ano%100!=0:
    print(f'O ano de {ano} é bissexto')

elif ano%400==0:
    print(f'O ano de {ano} é bissexto')

else:
    print(f'O ano de {ano} não é bissexto')
