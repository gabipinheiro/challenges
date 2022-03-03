# Challenge from Hacker Rank: Lily's Homework

# Problema:
# George quer sair com Lily, porém ela tem muitos deveres de casa e por isso ele vai ajudá-la a terminar mais rápido.
# Ele tem que resolver o seguinte problema: Recebendo um array com valores inteiros, diferentes e aleatórios,
# determinar qual é o mínimo de trocas (swaps) que devem ser feitas para que o arrey fique em ordem crescente.

# Exemplo:
# Vetor de entrada: arr = [7,15,12,3]
# 1ª troca: entre 3 e 7 = [3,15,12,7]
# 2ª troca: emtre 12 e 15 = [3,12,15,7]
# retorna mínimo de trocas = 2

# Solução:
# Varrer o vetor da esquerda para direita:
#   Seleciona a primeira posição:
#       varre o vetor novamente procurando se tem um numero menor que a posição atual
#       se tiver, realiza a troca, não mexe novamente na primeira posição e contabiliza troca
#       se não tiver, não realiza nenhuma troca e não mexe novamente na primeira posição
# o looping deve ocorrer até que o número atual esteja na última posição

from functools import reduce

def encontraMenorNumeroDeTrocas(arr):

    # numero de trocas inicia em 0
    swap = 0

    # tamanho do vetor recebido
    n = len(arr)
    ultima_pos = n-1

    #pos = 0
    #while pos != ultima_pos:

    for pos_i,i in enumerate(arr):

        #dif_pos_atual = i-pos_i
        #print('verifica: ',dif_pos_atual)

        menores = []

        # verifica se existe outro número na lista em que a diferença dê menor  que a diferença  anterior
        for pos_j,j in enumerate(arr):

            if pos_j <= pos_i:
                continue

            if j<i:
                menores.append(j)

        # encontra o menor número entre os menores que i e realiza a troca:
        encontra_menor = lambda x,y: x if x<y else y

        # se existir valores menores, verifica o menor e realiza a troca
        if menores:
            menor = reduce(encontra_menor, menores)

            # realiza a troca:
            pos_menor = arr.index(menor)
            pos_i = arr.index(i)

            arr[pos_menor] = i
            arr[pos_i] = menor

            swap = swap + 1

    print(swap,arr)
    return(swap)


#arr = [7,5,8,9,2,13,4,10,11]
#arr = [3,4,2,5,1]
arr = [7,15,12,3]
encontraMenorNumeroDeTrocas(arr)