
# -------------------------EXERCÍCIO 1----------------------------------------------
# for i in range(0, 10):
#     print(i)
# ---------------------------------------------------------------------------------



# -------------------------EXERCÍCIO 2----------------------------------------------
# x = 0
# for i in range(1, 10):
#     x += 1
#     print(i)
#     if i % 3 == 0:
#         i += 1
#         x -= 1
# print(x)
# ---------------------------------------------------------------------------------
    
    
num = 5

for i in range(num):
    linha = ''
    for j in range(i, -1, -1):
        linha += '* '

    print(linha)


    
