def imprimir_reverso(lista):
    pilha = []
    atual = lista
    while atual:
        pilha.append(atual.valor)
        atual = atual.proximo
    while pilha:
        print(pilha.pop())
