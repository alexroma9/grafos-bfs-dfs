from grafo import Grafo 
import random 
from math import sqrt

def distancia(NI, NF):
  x1 = NI.attributos['px']
  y1 = NI.attributos['py']
  x2 = NF.attributos['px']
  y2 = NF.attributos['py']
  dista = sqrt((x2-x1)**2 + (y2-y1)**2)
  return dista


def geosim(n,r):
  """
  Grafo Geografíco Simple (Método aleatorio)
  n : número de nodos.
  r : distancia para generar la arista entre dos nodos.
  """
  g = Grafo('GeoSimple')
  for i in range(n):
    nodo = g.addNodo(str(i))
    nodo.attributos['px'] = random.random()
    nodo.attributos['py'] = random.random() 
  conteoAristas = 1
  for i in range(n):
    for j in range(n):
      if i != j:
        nI = g.giveNodo(str(i))
        nF = g.giveNodo(str(j))
        dista = distancia(nI,nF)
        if dista <= r:
          g.addArista(str(conteoAristas),str(i),str(j))
          conteoAristas += 1  
  return g

print ("Modelo Geográfico simple  ----------")
n_nodo = int(input("Ingrese número de nodos: "))
dist = float(input("Ingrese la distancia máxima para crear un nodo valor entre 0 y 1: "))

geosim_ = geosim(n_nodo,dist)
n_inicia = list(geosim_.nodos.keys())[0]

arbolGeosim = Grafo.bfs(geosim_, n_inicia)
arbolGeosim.savedArchivo('{}_n{}'.format('_GeoSimple',str(n_nodo)))

eGraph = Grafo('DFSr')

path,arbolGeosim_r = Grafo.dfsr(geosim_, n_inicia,[],eGraph)
arbolGeosim_r.savedArchivo('{}_n{}'.format('_GeoSimple',str(n_nodo)))

arbolGeosim_i = Grafo.dfsi(geosim_, n_inicia)
arbolGeosim_i.savedArchivo('{}_n{}'.format('_GeoSimple',str(n_nodo)))




