"""
Tuplas sao, basicamente, lista IMUTAVEIS.
"""

# para declarar uma tuple, pode ser feito uma lista sem os colchetes

nomes = ("Leonardo", "Maria", "Helena")
print(nomes, type(nomes))

# tambem podemos fazer uma lista e depois converte-la para uma tuple

nomes2 = ["Leonardo", "Maria", "Helena"]
nomes2[2] = "Tupla"
nomes2 = tuple(nomes2)
print(nomes2, type(nomes2))

# para modificar uma tupla - o que nao e muito recomendavel - podemos transforma-la em uma lista, modificar o valor e transforma-la em tupla novamente
