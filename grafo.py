#from grafo import Grafo
from nodo import Nodo 
from arista import Arista 
neighbour = 'Vecino'
edge = 'Arista'


class Grafo():
  """
  Clase Grafo
  """
  def __init__(self, nombre):
    """
    Inicializa el grafo.
    nombre : Nombre del grafo.
    nodos
    aristas
    """
    self.id = nombre
    self.nodos = {} 
    self.aristas = {}
  
  def savedArchivo(self, sufijo):
    """
    Guarda datos de grafo en formato .gv
    Warning : Cuidado ya que sobre escribe una vez ejecutado el grafo solicitado.
    """
    file = open('{}{}.gv'.format(self.id, sufijo), 'w')
    file.write('digraph #nombre {' + '\n')
    for arista in self.aristas:
      #objetoArista = self.aristas[arista]
      #nodoInicial = objetoArista.inicio.id
      #nodoFinal = objetoArista.final.id
      file.write('{};'.format(arista) + '\n')
    file.write('}')
    file.close()

  def addNodo(self, nombreNodo):
    """
    Crea nodo , si esta creado no hace nada de lo contrario crea.
    """
    if nombreNodo in self.nodos:
        pass
    else:
      _nodo = Nodo(nombreNodo)
      self.nodos[nombreNodo] = _nodo
    return self.nodos[nombreNodo]
  
  def addArista(self, nombreArista, nombreNodoOrigin, nombreNodoDestino):
    """
    Crea arista, si esta creada no hace nada, de lo contrario crea.
    """
    if nombreArista in self.aristas:
        pass
    else:
        nodoOrigen = self.addNodo(nombreNodoOrigin)
        nodoDestino = self.addNodo(nombreNodoDestino)
        _arista = Arista(nombreArista,self.nodos[nombreNodoOrigin],self.nodos[nombreNodoDestino])
        self.aristas[nombreArista] = _arista
        nodoOrigen.attributos[neighbour].append(nodoDestino)
        nodoDestino.attributos[neighbour].append(nodoOrigen)
        nodoOrigen.attributos[edge].append(_arista)
        nodoDestino.attributos[edge].append(_arista)

  def giveNodo(self, nombre):
    return self.nodos[nombre]
  
  def givedegreesNodo(self, nombreNodo):
    """
    Entrega el grado del nodo considerado.
    """
    if not nombreNodo in self.nodos:
      print('Nodo no existe')

    else:
      _nodo = self.nodos[nombreNodo]
      grado = len(_nodo.attributos[neighbour])
      return grado
  
  def bfs(grafoGenerado, s):
      """
      BFS
      : parametro s : nodo fuente o root
      : g grafo generado por BFS
      """
      gbfs = Grafo('BFS')
      visitado = [s]
      cola = [s]
      diccionarioNodos = grafoGenerado.nodos
      while cola:
          m = cola.pop(0)
          for nodoAdjacente in diccionarioNodos[m].attributos['Vecino']:
              if nodoAdjacente.id not in visitado:
                  visitado.append(nodoAdjacente.id)
                  cola.append(nodoAdjacente.id)
                  gbfs.addArista('{} -- {}'.format(str(m), str(nodoAdjacente.id)),str(m),str(nodoAdjacente.id))     
      return gbfs

  def dfsr(grafoGenerado, nodoFuente, visitados, grafoDFSR):
      diccionarioNodos = grafoGenerado.nodos
      visitados.append(nodoFuente)
      for nodoAdjacente in diccionarioNodos[nodoFuente].attributos['Vecino']:
          if nodoAdjacente.id not in visitados:
              grafoDFSR.addArista('{} -- {}'.format(str(nodoFuente), str(nodoAdjacente.id)),str(nodoFuente),str(nodoAdjacente.id))     
              visitados,grafoDFSR = Grafo.dfsr(grafoGenerado, nodoAdjacente.id, visitados, grafoDFSR)
              #grafoDFSR = DFSR(grafoGenerado, nodoAdjacente.id, visitados, grafoDFSR)
      return visitados,grafoDFSR


  def dfsi(grafoGenerado, nodoFuente):
      """
      Funcion para generar un arbol DFS dado un grafo : grafoGenerado
      y un nodo inicio : nodoFuente
      Utilizamos el array visitados por que nodos hemos pasado
      DFS utiliza una pila para recorrer el grafo Last in First Out
      """

      gdfsi = Grafo('DFSi')
      diccionarioNodos = grafoGenerado.nodos 
      visitados = [nodoFuente]
      pila = [nodoFuente]
      while pila:
          m = pila.pop()
          if m not in visitados:
              visitados.append(m)
          for nodoAdjacente in diccionarioNodos[m].attributos['Vecino']:
              if nodoAdjacente.id not in visitados:
                  if nodoAdjacente.id not in pila:
                      pila.append(nodoAdjacente.id)

          if pila:
              ultimoNodo = pila[-1]
              gdfsi.addArista('{} -- {}'.format(str(m), str(ultimoNodo)),str(m),str(ultimoNodo))

      return gdfsi


