def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(origem, "->", destino)
    else:
        hanoi(n-1, origem, auxiliar, destino)
        print(origem, "->", destino)
        hanoi(n-1, auxiliar, destino, origem)
