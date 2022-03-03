# Challenge from Hacker Rank: New year chaos

# Problem:
# Varias pessoas estão na fila de uma roda gigante no dia de ano novo.
# Cada pessoa recebe uma etiqueta indicando a posição inicial na fila de 1 a n (n é a qtdd de pessoas na fila)
# Cada pessoa pode subornar até 2 pessoas na fila (apenas quem estiver exatamente na frente) para trocar de posição

# Será recebido um vetor, onde cada elemento vai significar a posição inicial de cada pessoa na fila e
# a posição de cada elemento indica a posição final da pessoa na fila.
# o programa deve retornar o número de subornos feitos. Se houve mais de 2 subornos, retornar a frase: "Too chaotic"

# Exemplo 1:
#   q = [1,2,3,5,4,6,7,8]
#   bribes = 1
#   retornar 1
# Exemplos 2:
#   q = [4,1,2,3]
#   bribes = 3
#   retornar "Too chaotic"


# Solução
# verifica se cada elemento está em sua devida posição inicial (devem estar em ordem crescente)
# para os elementos que não estão na posição inicial, verifica se:
#   à direita dele existe números menores que ele e
#   se existir, conta a quantidade de numeros (que será a quantidade de subornos para aquele elemento)
#   se a quantidaade de subornos para 1 elemento for maior que 2, printa "Too chaotic"
#   se nenehum elmento tiver mais de 2 subornos, soma a qtdd total de subornos e printa este total.


def minimumBribes(q):

    # houve suborno se:
    #   1. o elemento está fora de sua posição inicial e
    #   2. na sua direita, existir algum numero menor que este (a qtdd de numeros menores é a qtdd de suborno)

    # valores iniciais
    caos = False
    qtdd_suborno = 0
    ultima_pos = len(q)-1

    for pos_i,i in enumerate(q):

        # se o elemento esta fora da posicao inicial, verifica se houve suborno
        if i != pos_i+1:

            if pos_i != ultima_pos:

                # a variavel abaixo serve para verificar se houve mais de 3 subornos por elemento
                qtdd_suborno_por_elemento = 0

                # percorre o vetor da proxima posicao em diante e verifica quantos subornos houveram
                for pos_j,j in enumerate(q):

                    if pos_j<=pos_i:
                        continue

                    # a qtdd de subornos é igual à qtdd de elementos menores que ele, posicionados à direita dele
                    if j<i:
                        qtdd_suborno_por_elemento = qtdd_suborno_por_elemento + 1

                if qtdd_suborno_por_elemento > 2:
                    caos = True
                    print("Too chaotic")
                    break
                else:
                    qtdd_suborno = qtdd_suborno + qtdd_suborno_por_elemento

    if caos == False:
        print('subornos: ',qtdd_suborno)

q = [1,2,5,3,7,8,6,4]
#q = [5,1,2,3,7,8,6,4]
#q = [2,1,5,3,4]
#q = [4,1,2,3]
#q = [1,2,3,5,4,6,7,8]
#q = [2]

minimumBribes(q)
