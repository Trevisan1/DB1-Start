print('Digite uma letra e eu direi se é uma vogal ou consoante: ')

letra = str(input('Digite a letra: '))
letra = letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or  letra == 'u':
    print('É uma vogal')

else:
    print('É uma consoante')
