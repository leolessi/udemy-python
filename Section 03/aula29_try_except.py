"""

O try except permite a fluidez do código mesmo quando ele quebrar.
No caso do if/else, se o código quebrar antes do else, aparece apenas o código quebrado e não passa dali.

"""

numero_str = input("Vou dobrar o número que você digitar: ")

try:
    numero_float = float(numero_str)
    print(f"FLOAT: {numero_float}")
    print(f"O dobro de {numero_str} é {numero_float * 2} ")
except:
    print("Isso não é um número!")
