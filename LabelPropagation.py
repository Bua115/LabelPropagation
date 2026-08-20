import numpy
import math
import random
import networkx

def ObterVizinhos(A, i):
  V = sum(range(A))
  j = 0
  for i in range(A):
    if j == V:
       N(i) = 0
    else: 
       N(i) = 1

def CalcularModaEmpateAleatorio(RotulosVizinhos):
    

def LabelPropagation(A, maxIteracoes):
    #Inicialização
    N = NumeroDeVertices(A)
    Rotulos = numpy.array(0 in N-1)
    iteracao = 0
    RotulosMudaram = True

    while(Iteracao < maxIteracoes and RotulosMudaram):
        #Aleatorizar ordem dos vértices
        RotulosMudaram = False
        for i in range(N):
          OrdemVertices[i] = random.shuffle(N)
        # Obter vizinhos e calcular  
        for i in OrdemVertices:

            Vizinhos = ObterVizinhos(A, i) 
            if Vizinhos[i] != []:
               RotulosVizinhos = Rotulos[i]
               NovoRotulo = CalcularModaEmpateAleatorio(RotulosVizinhos)
               if NovoRotulo != Rotulos[i]:
                  Rotulos[i] = NovoRotulo
                  RotulosMudaram = True
        Iteracao = Iteracao + 1
    return Rotulos