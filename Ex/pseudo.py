num1_str = input("Digite o primeiro número de 4 dígitos: ")  
num2_str = input("Digite o segundo número de 4 dígitos: ")

# Verificar se os números tem exatamente 4 dígitos e se são numéricos
if len(num1_str) == 4 and len(num2_str) == 4 and num1_str.isdigit() and num2_str.isdigit():  
    # cria vetores (listas) com os dígitos invertidos (porque a multiplicação é feita da direita para a esquerda)
    OP1 = [int(num1_str[3 - i]) for i in range(4)] # OP1 será o vetor com os dígitos do num1
    OP2 = [int(num2_str[3 - i]) for i in range(4)] # OP2 será o vetor com os dígitos do num2
    
    print(f"OP1 (vetor de {num1_str}): {OP1}")
    print(f"OP2 (vetor de {num2_str}): {OP2}")

    # cria o vetor para armazenar o resultado da multiplicação, com espaço suficiente para armazenar até 8 pq 4*4=16
    # resultado = [0] * 8
    resultado = [0] * 8

    # multiplicação manual, existe o 'vai um' 
    for i in range(4): # Pra cada dígito de OP1
        vai_um = 0
        for j in range(4): # Para cada dígito de OP2
            # multiplicar os dígitos e somar com o valor que ja existe no vetor resultado,  -> 'vai um'
            mult = OP1[i] * OP2[j] + resultado[i + j] + vai_um
            print(f"Multiplicando {OP1[i]} e {OP2[j]}, somando com {resultado[i + j]} e o vai_um {vai_um}.")
            print(f"Resultado da multiplicação parcial: {mult} (vai para {mult % 10} e {mult // 10} de vai_um)")

            resultado[i + j] = mult % 10 # guardar o dígito da unidade
            vai_um = mult // 10 # guardar o 'vai um' para a próxima operação
            print(f"Resultado até agora: {resultado}")
        
        resultado[i + 4] += vai_um  
        print(f"Depois de adicionar o vai_um para a posição {i + 4}, o vetor resultado é: {resultado}")
    
    # resultado invertido (de trás pra frente, ignorando os zeros a esquerda)
    print("Resultado da multiplicação: ", end="")
    comecou = False
    for k in range(7, -1, -1): # Iniciar de trás para frente
        if resultado[k] != 0 or comecou: # enccontro primeiro dígito não zero, começa a imprimir
            print(resultado[k], end="")
            comecou = True

    if not comecou: # tudo zero só zerar
        print("0")
    else:
        print() # Ppula

else:
    print("Erro: ambos os números devem ter exatamente 4 dígitos.") # mensagem de erro por invalidade

