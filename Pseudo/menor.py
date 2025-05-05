'''
algoritmo OrganizaVetor(A)
    Para i começando do 0 até o penúltimo número do vetor:
        menorPosicao ← i
        Para j de i+1 até o último número do vetor:
            Se A[j] for menor que A[menorPosicao], então:
                menorPosicao ← j
        Se menorPosicao for diferente de i, então:
            guarda ← A[i]
            A[i] ← A[menorPosicao]
            A[menorPosicao] ← guarda
    Pronto, o vetor está em ordem
Fim
'''