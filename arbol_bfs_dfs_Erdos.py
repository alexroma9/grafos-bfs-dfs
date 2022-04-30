from grafo import Grafo
import random

def erdosrenyi(n,m, dirigido=False, auto=False):
  """
  Grafo Erdos-Renyi (método aleatorio)
  n : número de nodos
  m : número de aristas 
  """
  g = Grafo('Erdos-Renyi')
  for i in range(n):
    g.addNodo(str(i))
  for i in range(m):
    u = random.randint(0, n-1)
    v = random.randint(0, n-1)
    if u != v:
      g.addArista(str(i),str(u),str(v))
  return g


print ("Modelo Erdös y Rényi  ----------")
nodo = int(input("Ingrese número de nodos: "))
arista = int(input("Ingrese número de aristas: "))

erdosrenyi_ = erdosrenyi(nodo,arista)
n_inicia = list(erdosrenyi_.nodos.keys())[0]

arbolErdos = Grafo.bfs(erdosrenyi_, n_inicia)
arbolErdos.savedArchivo('{}_n{}'.format('_Erdos',str(nodo)))

eGraph = Grafo('DFSr')

path,arbolErdos_r = Grafo.dfsr(erdosrenyi_, n_inicia,[],eGraph)
arbolErdos_r.savedArchivo('{}_n{}'.format('_Erdos',str(nodo)))

arbolErdos_i = Grafo.dfsi(erdosrenyi_, n_inicia)
arbolErdos_i.savedArchivo('{}_n{}'.format('_Erdos',str(nodo)))

