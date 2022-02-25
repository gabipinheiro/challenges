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


def encontraMenorNumeroDeTrocas(arr):
    print(arr)

    # numero de trocas iniciando em 0
    swap = 0

    # pivot recebe primeiro elemento do vetor
    pivot = arr[0]

    # verificação ocorrerá até que o pivot seja a última posição do vetor
    ultima_posicao = len(arr) - 1
    while arr.index(pivot) != ultima_posicao:

        # varrendo o vetor da direita para a esquerda
        for i in reversed(arr):

            # se i for menor que pivot, realiza a troca e para iteração
            if i<pivot:
                pos_pivot = arr.index(pivot)
                pos_i = arr.index(i)

                arr[pos_pivot]=i
                arr[pos_i]=pivot

                swap = swap + 1

                pivot = i
                break

            if i == pivot:
                nova_pos_pivot = pos_pivot+1
                pos_pivot = nova_pos_pivot
                pivot = arr[pos_pivot]
                break

    print(swap,arr)
    return(swap)


#arr = [7,5,8,9,2,13,4,10,11]
arr = [3,4,2,5,1]
encontraMenorNumeroDeTrocas(arr)
