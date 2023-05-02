# media_doacoes = float(input("Informe a média de doações dos últimos 3 anos: "))   #c
# doacoes_atual = float(input("Informe o total de doações deste ano: "))

# excedente = doacoes_atual - media_doacoes                                         #b
# total = doacoes_atual*2                                                           #a

# if doacoes_atual > media_doacoes:                                                 #e
#    total += excedente * 3                                                         #f
#    print(f"O total em doações será R$ {total:.2f}")                               #d

#------------------------------------------------------------------------------------------------------------#

#x = -1
#y = 10
#z = 5

#if y > x < z and y != 0:
#    print('DB1 Start')

#------------------------------------------------------------------------------------------------------------#


# x = int(input("Digite o valor de x: "))
# y = int(input("Digite o valor de y: "))
# z = int(input("Digite o valor de z: "))

# if x > y ** 2 or z < 0:
#     print('A')

# elif z != y and x % 2 == 0:
#     print('B')

# elif z > x and y // x > 3:
#     print('C')

# else: print('D')

#------------------------------------------------------------------------------------------------------------#

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x < z < y:
    print("A")

elif x == y:
    print("B")

else:
    print("C")
    if y<0:
        print("D")
        w = '-' if z < 0 else '+'




