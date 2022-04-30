from nodo import Nodo

class Arista:
  def __init__(self, n_arista, nodo_fuente: Nodo, nodo_destino: Nodo):
    """
    Clase Arista
    n_arista : Nombre
    nodo_fuente : 
    nodo_destino :
    """
    self.id = n_arista
    self.inicio = nodo_fuente
    self.final = nodo_destino

