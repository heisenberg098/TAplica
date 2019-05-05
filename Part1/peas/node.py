
class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Crea un nodo de arbol de busqueda, derivado del nodo parent y accion action"""
        self.state = state  # posicion actual
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        """Devuelve los nodos alcanzables en un paso a partir de este nodo."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state, action, next_state))

    def solution(self):
        """Retorna la secuencia de acciones para ir de la raiz a este nodo."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Retorna una lista de nodos formando un camino de la raiz a este nodo."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
