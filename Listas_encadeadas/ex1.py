class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def contar_elementos(lista):
    contador = 0
    atual = lista
    while atual:
        contador += 1
        atual = atual.proximo
    return contador
