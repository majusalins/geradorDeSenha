import string
import random

caracteres = list(string.ascii_letters + string.digits + "!@#$%?^&*")

def gerar_senha_aleatoria():
    tamanho = int(input("Defina o número de dígitos da senha: "))
    random.shuffle(caracteres)

    senha = []
    for i in range(tamanho):
        senha.append(random.choice(caracteres))
    random.shuffle(senha)

    print("Aqui está sua senha gerada automaticamente: "+"".join(senha))

gerar_senha_aleatoria()