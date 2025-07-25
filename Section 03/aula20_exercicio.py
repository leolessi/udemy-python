primeiro_valor_str = input("Digite um valor: ")
segundo_valor_str = input("Digite outro valor: ")

int_primeiro_valor = int(primeiro_valor_str)
int_segundo_valor = int(segundo_valor_str)

if int_primeiro_valor > int_segundo_valor:
    print(f"{int_primeiro_valor = } maior que o {int_segundo_valor = }")
elif int_segundo_valor > int_primeiro_valor:
    print(f"{int_segundo_valor = } maior que o {int_primeiro_valor = }")
else:
    print("Valores iguais.")
