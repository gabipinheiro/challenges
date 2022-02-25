# Challenge

# Problema:
# Recebendo um array com valores inteiros, diferentes e aleatórios,
# retornar qual o número de trocas (swaps) para o array ficar em ordem crescecnte

# Solução: aplicação da técnica do Quicksort (pivô):
# 1. Selecionar o 1º elemento ('pivot') e varrer o vetor da direita para a esquerda até achar um número menor que ele;
# 2. realizar a troca entre estes dois números;
# 3. repetir os passos acima até que o pivô seja o número da ultima posicao do vetor.

def encontraNumeroDeTrocas(arr):

    # numero de trocas iniciando em 0
    swap = 0

    # pivot recebe primeiro elemento do vetor
    pivot = arr[0]

    # verificação ocorrerá até que o pivot seja a última posição do vetor
    ultima_posicao = len(arr) - 1
    while arr.index(pivot) != ultima_posicao:

        # varrendo o vetor da direita para a esquerda
        for i in reversed(arr):

            # se i for menor que pivot, realiza a troca e interrompe a iteração
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
encontraNumeroDeTrocas(arr)
