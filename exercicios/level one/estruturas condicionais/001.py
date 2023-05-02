print('Digite dois números e eu mostrarei o maior deles')

primeiro_numero = int(input('Digite o primeiro número: '))

segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > segundo_numero: 
    print('O maior número é: ', primeiro_numero)

elif primeiro_numero == segundo_numero:
    print('São iguais, digite de novo')

else: 
    print('O maior número é:', segundo_numero)
