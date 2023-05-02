print('Diga o preço de 3 produtos e eu direi qual deve comprar (o mais barato)')

produto_um = int(input('Digite o preço do primeiro: '))
produto_dois = int(input('Digite o preço do segundo: '))
produto_tres = int(input('Digite o preço do terceiro: '))


if produto_um < produto_dois < produto_tres or produto_um < produto_tres < produto_dois:
    print(f'O produto que deve comprar é o de valor: {produto_um}')

elif produto_dois < produto_um < produto_tres or produto_dois < produto_tres < produto_dois:
    print(f'O produto que deve comprar é o de valor: {produto_dois}')

elif produto_tres < produto_dois < produto_um or produto_tres < produto_um < produto_dois:
    print(f'O produto que deve comprar é o de valor: {produto_tres}')

else: 
    print('Existem produtos com o mesmo valor, não fiz condição pra isso')

