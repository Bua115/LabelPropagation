import numpy as np
import random
#Funcao para a obtencao dos vizinhos
def ObterVizinhos(N, i):
  Vizinhos = []
  for i in range(len(N)):
    if N[i] == 1:
      Vizinhos.append(i)
  return Vizinhos

def CalcularModaEmpateAleatorio(RotulosVizinhos):
   FrequenciaMaxima = max(np.bincount(RotulosVizinhos))
   NovoRotulo = random.choice(np.where(np.bincount(RotulosVizinhos) == FrequenciaMaxima)[0])
   return NovoRotulo 

def LabelPropagation(A, maxIteracoes):
     #Inicializacao (N = numero de vertices)
        iteracao = 0
        N = A
        Rotulos = np.array([N])
        RotulosMudaram = True
    
        while(iteracao < maxIteracoes and RotulosMudaram):
            #Aleatorizar ordem dos vertices
            OrdemVertices = N
            random.shuffle(OrdemVertices)
            RotulosMudaram = False
            # Obter vizinhos e calcular + verificar parada 
            for i in OrdemVertices:
                Vizinhos = ObterVizinhos(N, i) 
                for i in Vizinhos:
                    if i != []:
                        RotulosVizinhos = Rotulos[i]
                        NovoRotulo = CalcularModaEmpateAleatorio(RotulosVizinhos)
                    if NovoRotulo != Rotulos[i]:
                      Rotulos[i] = NovoRotulo
                      RotulosMudaram = True
            iteracao = iteracao + 1
        return Rotulos

# Leitura do arquivo com os dados e separação em vetores
with open(r"..\Data\rede1_duas_comunidades.csv", 'r') as f:
    Data = [line.strip().split(",") for line in f if line.strip()]
# Print dos resultados finais
print(f"Rótulos Finais: {LabelPropagation(Data, 100)}", )