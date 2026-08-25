import numpy as np
import random

from Visualizacao import (
    VisualizarRede,
    GraficoConvergencia,
    GraficoComunidades
)


#Funcao para a obtencao dos vizinhos
def ObterVizinhos(A, vertice):
    Vizinhos = []

    for j in range(len(A[vertice])):
        if A[vertice][j] == 1:
            Vizinhos.append(j)

    return Vizinhos


def CalcularModaEmpateAleatorio(RotulosVizinhos):
    Frequencias = np.bincount(RotulosVizinhos)
    FrequenciaMaxima = np.max(Frequencias)

    NovoRotulo = random.choice(
        np.where(Frequencias == FrequenciaMaxima)[0]
    )

    return NovoRotulo


def LabelPropagation(A, maxIteracoes):
    #Inicializacao (N = numero de vertices)
    iteracao = 0
    N = len(A)
    Rotulos = np.arange(N)
    RotulosMudaram = True

    HistoricoMudancas = []

    while(iteracao < maxIteracoes and RotulosMudaram):
        #Aleatorizar ordem dos vertices
        OrdemVertices = list(range(N))
        random.shuffle(OrdemVertices)

        RotulosMudaram = False
        QuantidadeMudancas = 0

        # Obter vizinhos e calcular + verificar parada
        for vertice in OrdemVertices:
            Vizinhos = ObterVizinhos(A, vertice)

            if len(Vizinhos) > 0:
                RotulosVizinhos = Rotulos[Vizinhos]
                NovoRotulo = CalcularModaEmpateAleatorio(RotulosVizinhos)

                if NovoRotulo != Rotulos[vertice]:
                    Rotulos[vertice] = NovoRotulo
                    RotulosMudaram = True
                    QuantidadeMudancas += 1

        HistoricoMudancas.append(QuantidadeMudancas)

        iteracao = iteracao + 1

    return Rotulos, HistoricoMudancas


# Leitura do arquivo com os dados e separação em vetores
with open("../Data/zachary.csv", "r") as f:
    Arestas = [
        tuple(map(int, line.strip().split(",")))
        for line in f
        if line.strip()
    ]

NumeroVertices = max(max(aresta) for aresta in Arestas) + 1

Data = np.zeros(
    (NumeroVertices, NumeroVertices),
    dtype=int
)

for origem, destino in Arestas:
    Data[origem][destino] = 1
    Data[destino][origem] = 1


RotulosIniciais = np.arange(len(Data))

VisualizarRede(
    Data,
    RotulosIniciais,
    "Rede antes da aplicação do Label Propagation"
)


RotulosFinais, HistoricoMudancas = LabelPropagation(
    Data,
    100
)


VisualizarRede(
    Data,
    RotulosFinais,
    "Rede após a aplicação do Label Propagation"
)


GraficoConvergencia(HistoricoMudancas)


GraficoComunidades(RotulosFinais)


# Print dos resultados finais
print(f"Rótulos Finais: {RotulosFinais}")
print(f"Número de comunidades: {len(np.unique(RotulosFinais))}")
print(f"Número de iterações: {len(HistoricoMudancas)}")