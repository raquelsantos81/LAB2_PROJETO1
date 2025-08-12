print ("Hello World")]

import random 

def cumprimento (texto):
    return f"Olá {texto}"

def media_7_numeros():
    numeros = [random.randint(1, 100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return numeros, media


if __name__ == "__main__":
    nome_completo = "Raquel Santos"
    print (cumprimento(nome_completo))
    numeros, media = media_7_numeros()
    print(f"Números sorteados: {numeros}")
    print(f"Média dos números: {media}")

