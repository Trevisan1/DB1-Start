print('Digite três números e eu irei mostrar o maior e o menor deles')

numero_um = int(input('Digite o primeiro número: '))
numero_dois = int(input('Digite o segundo número: '))
numero_tres = int(input('Digite o terceiro número: '))

if numero_um > numero_dois and  numero_um > numero_tres:
    print(f"O maior número é: {numero_um} e o menor número é: {numero_tres}")

elif numero_um > numero_tres and numero_um > numero_dois:
    print(f"O maior número é: {numero_um} e o menor número é: {numero_dois}")

elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"O maior número é: {numero_dois} e o menor número é: {numero_tres}")
   
elif numero_dois > numero_tres and numero_dois > numero_um:
    print(f"O maior número é: {numero_dois} e o menor número é: {numero_tres}")

elif numero_tres > numero_um and numero_tres > numero_dois:
    print(f"O maior número é: {numero_tres} e o menor número é: {numero_dois}")

elif numero_tres > numero_dois and numero_tres > numero_um:
    print(f"O maior número é: {numero_tres} e o menor número é: {numero_um}")

else:
    print('Existem números iguais, refaça')
