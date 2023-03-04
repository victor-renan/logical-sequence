# Victor Renan Alves de Oliveira
# 04/03/2023

def obterPrimosAte(num):
    # Gera uma lista vazia
    conjunto_primos = []

    # Para cada numero de (1-1) a (20-1)
    for i in range(num):
        # Soma o 1 que foi tirado
        i = i+1

        # Se i nao for 1
        if i != 1:
        # Cada numero gerado eh adicionado na lista
            conjunto_primos.append(i)

        # Para cada numero de (1-1) a (i-1)
        for j in range(i):
            # Soma o 1 que foi tirado
            j = j+1
            # Se i não for 1 nem ele mesmo
            if (i != j and j != 1):
                # Se o resto da divisao for 0
                if (i % j) == 0:
                    # Se i estiver na lista
                    if i in conjunto_primos:
                        #i eh removido, restando apenas os primos
                        conjunto_primos.remove(i)

    # Retorna o conjunto
    return conjunto_primos


# Obtem quantidade de primos (n)
def obterQuantPrimos(quantidade):
    # Define um indice a partir do 1o numero primo (2)
    num = 2

    # Cria uma lista (conjunto) vazia
    primos_obtidos = []

    # Se a quantidade nao for 0
    if quantidade != 0:
        # Enquanto o tamanho da lista for menor que a quantidade proposta
        while len(primos_obtidos) < quantidade:
            # Soma-se uma unidade ao indice
            num = num + 1

            # Verifica os primos de num + 1
            primos_obtidos = obterPrimosAte(num)
    
    # Retorna os (n) primos obtidos
    return primos_obtidos


# Gera a sequencia propriamente dita
def obterSequencia(quantidade):
    # Cria-se uma lista (conjunto) vazia
    sequencia = []

    # Se quantidade nao for 0
    if quantidade != 0:
        # A sequencia se inicia com o 1
        sequencia = [1]

        # Para cada numero na quantidade, menos o 1 (que ja esta no conjunto)
        for i in range(quantidade-1):
            '''

            A sequencia adiciona com base na logica:
                    Nsx = (NSx-1 + NPx-1) * 2
            Isto considerando que x > 1, pois NS1 = 1 (Primeiro numero da sequencia),
            tomando tambem NP = {2, 3, 5, 7, 11, ...} (Conjunto dos primos)

            Logo, por exemplo: NS2 = (NS2-1 + NP2-1) * 2 ->
                    NS2 = (1 + 2) * 2 = 6
                    NS3 = (6 + 3) * 2 = 18
                    NS4 = (18 + 5) * 2 = 46
                        etc...
            '''
            # Adiciona o numero na sequencia
            sequencia.append((sequencia[i]
                + obterQuantPrimos(quantidade)[i]) * 2)
            
    # Retorna a sequencia
    return sequencia

print(obterSequencia(20))