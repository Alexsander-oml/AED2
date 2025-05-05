class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def imprimir_maiores_que_media(inicio):
    # Primeiro: calcular a média
    soma = 0
    cont = 0
    atual = inicio

    while atual:
        soma += atual.valor
        cont += 1
        atual = atual.proximo

    if cont == 0:
        print("Lista vazia.")
        return

    media = soma / cont

    # Segundo: imprimir pares (posição, valor) onde valor > média
    atual = inicio
    posicao = 0

    print(f"Valores maiores que a média ({media:.2f}):")
    while atual:
        if atual.valor > media:
            print(f"({posicao}, {atual.valor})")
        atual = atual.proximo
        posicao += 1