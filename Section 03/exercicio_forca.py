# - pegar a letra do usuário
# - verificar se foi apenas uma letra fornecida, caso SIM, continuar o programa. Caso não, retornar o programa para a pergunta
# - verificar se a letra fornecida pelo usuário está na palavra secreta. Caso esteja, salvar essa letra em uma nova string junto com as letras que estão no segredo (letras_contidas_no_segredo)
# - percorrer as letras do segredo (for letra_secreta in segredo). Se a letra secreta for igual a letra fornecida, printar a letra fornecida. Se não for, printar um asterisco
# - para printar tudo em uma linha, iterar o print acima em uma nova string (nova frase += letra fornecida / nova frase += "*"
# - para não ter que percorrer o loop inteiro, verificar se a letra fornecida já faz parte da string letras_contidas_no_segredo
# - calcular o numero de tentativas (talvez limitar)

segredo = "segredo".upper()
letras_contidas_no_segredo = ""
tentativas = 0

while True:
    letra_fornecida = input("Digite a letra: ").upper()
    tentativas += 1

    if len(letra_fornecida) > 1:
        print("Digite apenas uma letra!")
        continue

    if letra_fornecida in segredo:
        if letra_fornecida in letras_contidas_no_segredo:
            continue
        else:
            letras_contidas_no_segredo += letra_fornecida

    nova_palavra = ""
    for letra_secreta in segredo:
        if letra_secreta in letras_contidas_no_segredo:
            nova_palavra += letra_secreta
        else:
            nova_palavra += "*"

    print(nova_palavra)
    if nova_palavra == segredo:
        break

print(
    f"Você adivinhou a palavra secreta '{segredo.upper()}' em {tentativas} tentativas."
)
