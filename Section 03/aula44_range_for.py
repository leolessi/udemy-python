"""
For + Range
range -> range(start, stop, step)
"""

# A lista retornada vai de 1 até 10 pois a função range(start, stop, step) não inclui o valor do argumento stop. O intervalo gerado pelo range é semiaberto, ou seja, inclui o start e vai até o valor imediatamente anterior ao stop - que, no caso, é o 10.

# numeros = range(1, 11)
# escolhas = []

# for numero in numeros:
#     escolhas.append(numero)

# print(escolhas)
#
#
linha_tabela = []
for i in range(10):
    if i == 4:
        continue

    for j in range(0, 3, 2):
        # para range(3)
        # if j == 1:
        #     continue

        linha_tabela.append(f"[{i},{j}]")
    print(linha_tabela)
    linha_tabela = []
