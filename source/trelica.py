from source.codificador import codificar
# Criação da treliça da máquina de estados

def criarTrelica(m, G):
    # m -> Quantidade de memórias
    # G -> Conjunto de polinômios geradores
    # treliça -> (M, u, V, MF)
    # Criar o conjunto de memórias
    M = []
    # trelica
    trelica = []
    alpha = [0, 1]
    if m == 3:
        M = [[a, b, c] for a in alpha for b in alpha for c in alpha]
    elif m == 4:
        M = [[a, b, c, d] for a in alpha for b in alpha for c in alpha for d in alpha]
    else:
        M = [[a, b, c, d, e] for a in alpha for b in alpha for c in alpha for d in alpha for e in alpha]

    # Realizar a codificação de cada memória possível para cada entrada possível
    for m in M:
        for u in alpha:
            mfaux = []
            V = [0, 0, 0]
            codificar(u, G, m, V, mfaux)
            trelica.append((m, u, V, mfaux))
    return trelica



if __name__ == "__main__":
    G = [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    m = 3
    trelica = criarTrelica(m, G)
    for element in trelica:
        print(element)
