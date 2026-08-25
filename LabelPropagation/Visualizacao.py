import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def VisualizarRede(A, Rotulos, titulo):
    G = nx.from_numpy_array(A)

    Posicoes = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nx.draw(
        G,
        Posicoes,
        with_labels=True,
        node_color=Rotulos,
        cmap="tab10",
        node_size=800,
        font_size=12,
        edge_color="gray"
    )

    plt.title(titulo)
    plt.show()


def GraficoConvergencia(HistoricoMudancas):
    Iteracoes = range(1, len(HistoricoMudancas) + 1)

    plt.figure(figsize=(8, 5))

    plt.plot(
        Iteracoes,
        HistoricoMudancas,
        marker="o"
    )

    plt.xlabel("Iteração")
    plt.ylabel("Quantidade de mudanças")
    plt.title("Convergência do Label Propagation")

    plt.grid(True)
    plt.show()


def GraficoComunidades(Rotulos):
    Comunidades, Tamanhos = np.unique(
        Rotulos,
        return_counts=True
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        Comunidades.astype(str),
        Tamanhos
    )

    plt.xlabel("Comunidade")
    plt.ylabel("Quantidade de vértices")
    plt.title("Tamanho das comunidades")

    plt.show()