
class MapSearchProblem():

    def __init__(self, initial, goal, mapPitts):
        """ El constructor recibe  el estado inicial, el estado
            objetivo y un mapa (de clase Mapa)
        """
        self.initial = initial
        self.goal = goal
        self.map = mapPitts

    def actions(self, state):
        """ Retorna las acciones ejecutables desde ciudad state.
            El resultado es una lista de strings tipo 'goCity'. 
        """
        neighbors = []
        acciones = []
        tupla = ()        
        neighbors = self.map.neighbors[state]
        for acc in range(len(neighbors)):
            acciones.append('go' + neighbors[acc][0])
        return acciones

    def result(self, state, action):
        """ Retorna el estado que resulta de ejecutar la acción dada desde ciudad state.
            La acción debe ser alguna de self.actions(state).
        """  
        new_state = action[2]
        return new_state

    def goal_test(self, state):
        return self.goal == state

    def path_cost(self, c, state1, action, state2):
        """Retorna el costo del camino de state2 viniendo de state1 con la acción action 
        El costo del camino para llegar a state1 es c. El costo de la acción debe ser
        extraído de self.map."""
        action_cost = 0
        dest_states = self.map.neighbors[state1] # estado destino, state2
        
        for acc in range(len(dest_states)):
            if dest_states[acc][0] == state2:
                action_cost = dest_states[acc][1]
                break

        return c + action_cost
