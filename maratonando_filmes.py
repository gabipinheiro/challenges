# DESAFIO: Nubank - Yes, She Codes 2022

# PROBLEMA: Alex ganhou uma coleção de filmes para maratonar no mínimo de dias possíveis.

# Restrições do problema:
# - ela pode assistir no máximo 3 horas por dia
# - ela não vê filme de forma particionada, ou seja, ela começa e termina no mesmo dia
# - duração mínima de cada filme = 1,01
# - duração máxima de cada filme = 3,00

# SOLUÇÃO (steps):
# 1. reordenar o vetor 'duracoes' em ordem descrescente;
# 2. enquanto o tamanho do vetor 'nao_vistos' for diferente de 0 (até todos os filmes disponiveis serem vistos):
# 3. pega a primeira posição do vetor 'duracoes' e:
#   4. verifica a duração faltante para o dia (= 3 - duração_atual) // será chamada de 'duração_faltante'
#   5. varre o vetor 'durações' e verifica:
#       6. se tem alguma duração igual à faltante;
#       7. se não, insere os filmes com duração menor igual à duração faltante em um vetor // 'possibilidades_do_dia'
#       8. a partir do maior, verifica quais durações (somando), chegam proximo do valor faltante
# obs:
# conforme os filmes forem sendo selecionados:
#   exclui do 'nao_vistos'
#   insere o somatorio dos filmes do dia no vetor 'vistos'
# no final (quando o vetor 'nao_vistos' zerar), o numero de dias será o tamanho do vetor 'vistos'
# retorn 'dias'

# --------------------------------------------------------------------------------------------

# variaveis fixas
# maximo e minimo de tempo (em horas) possivel a ser gasto por dia assistindo filmes
max_dia = 8
min_dia = 1

# variavel teste
duracoes = [4, 3, 1, 5, 2, 1, 7, 8, 2, 4, 6]

def encontrarMinimoDeDias(duracoes):

    # vetor para inserir apenas os filmes possíveis de serem vistos (dentro do limite estabelecido)
    filmes_colecao = [x for x in duracoes if x in range(min_dia,max_dia+1)]
    filmes_colecao.sort(reverse=True) # reordenando para otimizar o algoritmo

    # 'não vistos' inicia com o conteúdo de 'filmes_colecao' e conforme forem sendo vistos, serão removidos de 'nao_vistos'
    nao_vistos = [x for x in filmes_colecao]

    # o vetor 'vistos' inicia zerado e cada valor vai representar a duração de filmes vistos por dia
    # obs: a soma de todos os elementos deste vetor deve ser igual à soma da duração total de 'filmes a serem vistos'
    vistos = []

    while len(nao_vistos) != 0:

        for i in filmes_colecao:

            if i not in nao_vistos:
                continue

            nao_vistos.remove(i)

            duracao_faltante = max_dia-i;
            possibilidades_do_dia = [x for x in nao_vistos if x <= duracao_faltante]
            print('possibilidades do dia antes de reorderar: ',possibilidades_do_dia)

            # verifica se falta filme para completar o dia
            if len(possibilidades_do_dia) == 0: # se não, já adiciona o filme atual em 'vistos' e fecha o dia
                vistos.append(i)
            else: # se ainda faltar, verifica quais filmes irão se encaixar
                selecionadas = encontrarFilmesFaltantes(possibilidades_do_dia,duracao_faltante)

                # remove filmes do vetor 'não vistos' e soma duração dos filmes a serem vistos no dia
                soma = i
                for j in selecionadas:
                    nao_vistos.remove(j)
                    soma = soma + j

                # acrescenta soma dos filmes do dia no vetor 'vistos'
                vistos.append(soma)

    # a quantidade de elementos de 'vistos' é a quantidade mínima de dias para ver todos os filmes
    dias = len(vistos)
    print('Mínimo de dias será: ',dias)

    return(dias)

# função que vai encontrar os filmes que faltam para completar o dia
# recebe a duração que falta e retorna quais durações foram selecionadas
def encontrarFilmesFaltantes(possibilidades_do_dia,duracao_faltante):
    soma = 0
    selecionadas = [] # usado para inserir as durações selecionadas para completar o dia (este será o vetor retornado)

    for i in possibilidades_do_dia:
        if i == duracao_faltante:
            selecionadas.append(i)
            break
        if soma+i <= duracao_faltante:
            soma = soma + i;
            selecionadas.append(i)
    return(selecionadas)


encontrarMinimoDeDias(duracoes)










