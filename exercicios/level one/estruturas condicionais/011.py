print('Me forneça os valores de a, b e c da equação ax² + b + c, e eu direi as raízes')

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = (b**2 - 4 * a * c)**1/2

x_um = (- b + delta)/2*a

x_dois = (- b - delta)/2*a

print(f'O valor das raízes são X1: {x_um}  X2: {x_dois}')


