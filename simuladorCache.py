import numpy as np
import os

tamBloco = 4
linConjunto = 2
tamCache = 8
tamMP = 128
tamCelula = 8
hits = 0
misses = 0
clear = lambda: os.system('clear')
memoriaPrincipal = np.random.randint(0,(2**tamCelula) - 1,tamMP)  #gera uma lista com numeros aleatórios entre 0 e 255
for item in memoriaPrincipal:  #transforma os numeros em binários de 8 bits
    item = format(item,'08b')


memoriaCache = []
i = 0
while i < tamCache:
    memoriaCache.append(format(0,'039b'))
    i+= 1
print("len",len(memoriaCache[0]))
def polSubstituicao(linha):
    if(linha % 2 == 0):
        vish = memoriaCache[linha][2:]
        aux2 = memoriaCache[linha][0]
        memoriaCache[linha] = aux2 + str(1) + vish
        vish = memoriaCache[linha+1][2:]
        aux2 = memoriaCache[linha+1][0]
        memoriaCache[linha+1] = aux2 + str(0) + vish
    else:
        vish = memoriaCache[linha][2:]
        aux2 = memoriaCache[linha][0]
        memoriaCache[linha] = aux2 + str(1) + vish
        vish = memoriaCache[linha-1][2:]
        aux2 = memoriaCache[linha-1][0]
        memoriaCache[linha - 1] = aux2 + str(0) + vish


def leitura (endereco):
    print(endereco)
    conjunto = int(endereco[3:5],2)
    bloco = int(endereco[:5],2) # descobrindo o numero do bloco
    i = conjunto
    aux = 0
    while i <= conjunto + 1 : # passa pelo conjunto da cache
        if (str(memoriaCache[i][2:7]) == str(endereco[:5])) and (memoriaCache[i][0] == "1"): # se o endereço está na memória cache
            substituicao = i
            global hits
            hits  = hits + 1
            aux += 1
            print("Hit!\n")
            inteiro = int(endereco[5:],2) + 1 # pegando o deslocamento
            polSubstituicao(i)
            print("Valor :",memoriaCache[i][7 * (inteiro) -1 :7 * (inteiro) + 7])
        i = i + 1

    if(aux == 0): # se for 0 não encontrou o bloco na cache
        global misses
        misses = misses + 1
        print("Miss!\n")
        i = conjunto * linConjunto
        while i <= conjunto * linConjunto + 1: #passa pelo conjunto da cache
            if memoriaCache[i][1] == "0": # se o valor for 0 quer dizer que é o mais antigo na cache
                substituicao = i
            i = i + 1
        i = bloco * tamBloco
        print("Bloco = ",bloco)
        print("tam bloco",tamBloco)

        meudeus = "1"+"1"+str(format(bloco,'05b'))
        while i < (bloco * tamBloco) + tamBloco:
            print("i = ", i)
            meudeus = meudeus + str(format(memoriaPrincipal[i],'08b'))

            i += 1
        memoriaCache[substituicao] = meudeus
        polSubstituicao(substituicao)

    print("Bloco da memória principal : ",bloco)
    print("Conjunto : ",conjunto)
    print("Linha do conjunto : ",substituicao)



def Escrita(endereco):

    leitura(endereco)
    escrever = input("Digite o valor a ser escrito na memória:")
    escrever = int(escrever,2)
    memoriaPrincipal[int(endereco,2)] = escrever
    escrever = format(escrever,'08b')
    conjunto = int(endereco[3:5],2)
    i = conjunto
    while i <= conjunto * 2 + 1:
        if (str(memoriaCache[i][2:7]) == str(endereco[:5])):
            linha = i
        i = i + 1
    print("linha",linha)
    inteiro = int(endereco[5:],2) + 1
    print("COnjunto :",conjunto)
    copia = memoriaCache[linha][:7 * (inteiro)]
    copia2 = memoriaCache[linha][7 * (inteiro) + 8:]
    clear()
    memoriaCache[linha] = str(copia) + str(escrever) + str(copia2)
    print("Valor escrito na memória : ",str(escrever),"\n\n")



def stats():
    global hits
    global misses
    print("Hits :  ",hits)
    print("Misses : ",misses)
    print("Porcentagem de acerto: ",100/(hits+misses) * hits,"%")



def exibir():
    a = input("h para hexadecimal, d para decimal, b para Binário:")
    if(a == "h"):
        print("Memória principal")
        i = 0
        while i < len(memoriaPrincipal):
            print(format(i,'02X')," ",format(memoriaPrincipal[i],'02X'))
            i = i + 1
        print("\n\nMemória Cache")
        i = 0
        while i < len(memoriaCache):
            print(format(i,'X')," ",format(int(memoriaCache[i],2),'9X'))
            i = i + 1
    elif(a == "d"):
        print("Memória principal")
        i = 0
        while i < len(memoriaPrincipal):
            print(format(i,'03d')," ",format(memoriaPrincipal[i],'03d'))
            i = i + 1
        print("\n\nMemória Cache")
        i = 0
        while i < len(memoriaCache):
            print(format(i,'01d')," ",format(int(memoriaCache[i],2),'012d'))
            i = i + 1
    else:
        print("Memória principal")
        i = 0
        while i < len(memoriaPrincipal):
            print(format(i,'07b')," ",format(memoriaPrincipal[i],'08b'))
            i = i + 1
        print("\n\nMemória Cache")
        i = 0
        while i < len(memoriaCache):
            print(format(i,'03b')," ",format(int(memoriaCache[i],2),'039b'))
            i = i + 1




cond = 0
while (cond != 5):
    print('1 : Ler um endereço da memória\n2 : Escrever na memória\n3 : Apresentar as estatísticas\n4 : Printar memórias \n5 : Sair do programa')
    cond = input()
    print(cond)
    if cond == "1":
        clear()
        poxa = str(input("Digite o endereço a ser lido\n"))
        leitura(poxa)
        continue
    elif cond == "2":
        clear()
        poxa = str(input("Digite o endereço a ser escrito\n"))
        Escrita(poxa)
        continue
    elif cond == "3":
        clear()
        stats()
        continue
    elif cond == "4":
        clear()
        exibir()
        continue
    elif cond == "5":
        break
    else:
        clear()
        print("Opção inválida\n")
        continue
