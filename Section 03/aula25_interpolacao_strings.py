"""
Interpolação básica de strings
%s - string
%d e %i - int
%f - float
%x e %X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Leonardo"
idade = 27
preco = 1000.98124981
variavel = "%s, o preço é R$%.2f" % (nome, preco)
variavel_2 = "Sua idade é: %i" % (idade)
print(variavel)
print(variavel_2)
print("O hexadecimal de %d é %08x" % (1500, 1500))
