from grafo import Grafo
import random

edge = 'Aristas'
neighbour = 'Vecinos'

def barabasi(n,d):
  """
  Grafo Barabasi (Método aleatorio)
  n : número de nodos.
  d : número de aristas máximas por nodo.
  """
  g = Grafo('Barabasi-Albert')
  g.addNodo(str(0))

  Aristas = 1
  for i in range(1, n):
    nodosRandom = randomA(i)
    for j in range(i):
      grado = g.givedegreesNodo(str(nodosRandom[j]))
      pr = 1 - grado / d 
      #print(grado, d, pr)
      if random.random() < pr:
        if nodosRandom[j] != i:
          g.addArista(Aristas, str(i), str(nodosRandom[j]))
          Aristas += 1
  
  return g


def randomA(tamano):
  """
  Forma un arreglo aleatorio para generar el grafo Barabasi
  """
  num = []
  res = []
  t = tamano
  for i in range(tamano):
    num.append(i)
  for i in range(tamano):
    aleatorio = random.randint(0,t-1)
    res.append(num[aleatorio])
    num.pop(aleatorio)
    t = t - 1

  return res


print ("Modelo Barabasi  ----------")
nodo = int(input("Ingrese número de nodos: "))
aris = int(input("Ingrese número de arista: "))

barabasi_ = barabasi(nodo,aris)
n_inicia = list(barabasi_.nodos.keys())[0]

arbolBarabasi = Grafo.bfs(barabasi_, n_inicia)
arbolBarabasi.savedArchivo('{}_n{}'.format('_Barabasi',str(nodo)))

eGraph = Grafo('DFSr')

path,arbolBarabasi_r = Grafo.dfsr(barabasi_, n_inicia,[],eGraph)
arbolBarabasi_r.savedArchivo('{}_n{}'.format('_Barabasi',str(nodo)))

arbolBarabasi_i = Grafo.dfsi(barabasi_, n_inicia)
arbolBarabasi_i.savedArchivo('{}_n{}'.format('_Barabasi',str(nodo)))

