neighbour = 'Vecino'
edge = 'Arista'
class Nodo:
  def __init__(self, n_nodo):
    """
    Clase Nodo
    n_nodo : Nombre del nodo.
    attibutos : neighburn - Vecino
                edge      - Arista
    """
    self.id = n_nodo
    self.attributos = {
            neighbour: [],
            edge:[]
    }
