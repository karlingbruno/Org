import numpy as np
memoriaPrincipal = np.random.randint(0,255,128)  #gera uma lista com numeros aleatórios entre 0 e 255
for item in memoriaPrincipal:  #transforma os numeros em binários de 8 bits
    item = format(item,'08b')

memoriaCache = []
i = 0
while i <= 7:
    memoriaCache.append(format(0,'032b'))
    i+= 1

tamBloco = 4

linConjunto = 2
'''
for item in memoriaPrincipal:    #printa em hexadecimal
   print(format(item,'02X))
'''
'''
cond = 0
while (cond != 4):

    print('1 : Ler um endereço da memória\n2 : Escrever na memória\n3 : Apresentar as estatísticas\n4 : Sair do programa') 
    input(cond)

    if (cond == 1):

    elif (cond == 2):

    elif (cond == 3):

    elif (cond == 4)

    else:
        print("Opção inválida\n")

'''