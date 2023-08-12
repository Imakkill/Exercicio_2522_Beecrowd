import math
import heapq

# Definição de uma posição de computador
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Função para calcular a distância euclidiana entre duas posições de computadores
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Função para calcular o comprimento total mínimo de cabo de rede necessário usando o algoritmo de Prim
def minimumCableLengthPrim(computers):
    n = len(computers)

    # Inicialização
    inTree = [False] * n
    minDist = [float('inf')] * n

    # Começando a partir do primeiro computador (arbitrariamente)
    minDist[0] = 0.0
    totalCableLength = 0.0

    # Usando um heap (fila de prioridade) para manter os vértices com menor distância na frente
    pq = [(0.0, 0)]  # Inserir primeiro vértice

    while pq:
        dist, u = heapq.heappop(pq)

        if inTree[u]:
            continue

        inTree[u] = True
        totalCableLength += minDist[u]

        for v in range(n):
            if not inTree[v]:
                weight = distance(computers[u], computers[v])
                if weight < minDist[v]:
                    minDist[v] = weight
                    heapq.heappush(pq, (minDist[v], v))

    return totalCableLength

def main():
    while True:
        try:
            n = int(input())
            computers = []
            for _ in range(n):
                x, y = map(int, input().split())
                computers.append(Point(x, y))

            result = minimumCableLengthPrim(computers)
            print(f"{result:.2f}")

        except EOFError:
            break

if __name__ == "__main__":
    main()