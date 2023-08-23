from random import choice
from palavras import frutas


palavra_secreta = choice(frutas)
resposta_atual = ["_"]*len(palavra_secreta)
tentativas = 6
erros = []


while True:
    print(" ".join(resposta_atual))
    print(f"Tentativas restantes: {tentativas}")
    print(f"Erros: {' - '.join(erros)}")

    entrada_usuario = input("Digite uma letra: ")
    acertou = False

    for index, letra_secreta in enumerate(palavra_secreta):
        if entrada_usuario == letra_secreta:
            resposta_atual[index] = entrada_usuario
            acertou = True

    if not acertou:
        tentativas -= 1
        erros.append(entrada_usuario)

    if tentativas == 0:
        print("Você perdeu!!!")
        print(f"A palavra era {palavra_secreta}")
        break

    if "".join(resposta_atual) == palavra_secreta:
        print("Você ganhou!!!")
        break
print(" ".join(resposta_atual))
print(f"Erros: {' - '.join(erros)}")
