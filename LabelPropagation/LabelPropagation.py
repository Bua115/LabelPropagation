import numpy as np
import random

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

    while(iteracao < maxIteracoes and RotulosMudaram):
        #Aleatorizar ordem dos vertices
        OrdemVertices = list(range(N))
        random.shuffle(OrdemVertices)

        RotulosMudaram = False

        # Obter vizinhos e calcular + verificar parada
        for vertice in OrdemVertices:
            Vizinhos = ObterVizinhos(A, vertice)

            if len(Vizinhos) > 0:
                RotulosVizinhos = Rotulos[Vizinhos]
                NovoRotulo = CalcularModaEmpateAleatorio(RotulosVizinhos)

                if NovoRotulo != Rotulos[vertice]:
                    Rotulos[vertice] = NovoRotulo
                    RotulosMudaram = True

        iteracao = iteracao + 1

    return Rotulos


# Leitura do arquivo com os dados e separação em vetores
with open(r"..\Data\rede1_duas_comunidades.csv", 'r') as f:
    Data = [line.strip().split(",") for line in f if line.strip()]

Data = np.array(Data, dtype=int)

# Print dos resultados finais
print(f"Rótulos Finais: {LabelPropagation(Data, 100)}")