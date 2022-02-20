# Problem:
# Um bolo de aniversário terá o número de velas igual à idade do aniversariante.
# Apenas as velas maiores poderão ser apagadas.
# Verificar quantas velas serão apagadas levando em conta o tamanho de cada vela.

# Variaveis de entrada:
# candles = [], onde cada elemento será o tamanho de uma vela

# Solution:
# 1. ordenar as velas de forma decrescente
# 2. verificar qual é primeiro número (x)
# 3. verificar quantos são os elementos iguais ao primeiro número
# 4. retornas quantidade de números

#---------------------------------------------------------------

def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    tallest_candles = candles.count(candles[0])

    return (tallest_candles)

candles = [3,2,1,3]
birthdayCakeCandles(candles)