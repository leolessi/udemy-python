"""

Fatiamento de strings
+012345678
 Ola mundo
-987654321

Fatiamento [i:f:p] [::]
     inicio:final:passo

"""

variavel = "Ola mundo"
tamanho_variavel = len(variavel)

print(variavel[-4])
print(variavel[5])
print(variavel[2:5])
print(variavel[4:])
print(variavel[:3])
print(f"A variavel tem {tamanho_variavel} caracteres")
print(variavel[-1 : -(tamanho_variavel + 1) : -1])
