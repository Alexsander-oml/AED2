def listas_iguais(lista1, lista2):
    atual1 = lista1
    atual2 = lista2
    while atual1 and atual2:
        if atual1.valor != atual2.valor:
            return False
        atual1 = atual1.proximo
        atual2 = atual2.proximo
    return atual1 is None and atual2 is None