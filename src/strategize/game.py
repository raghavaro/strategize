from src.strategize.analysis import *

class Game:

    '''
    Game currently represents a normal form game
    
    ## Artificial Limits
    
    - player_set = 2
    - action_set = 2 per player

    Artifical limts are imposed for easy representation
    Limits will be lifted in future releases
    '''

    def __init__(self, player_set, action_set, utility_set):
        num_players = player_set.shape[0]
        print('Initializing a {} player game'.format(num_players))
        self.N = player_set
        self.A = action_set
        self.u = utility_set
    
    def __repr__(self):
        return '''Game (N, A, u) where 
    N = {}
    A = {}
    u = {}'''.format(self.N, self.A, self.u)

    def analyze(self):
        return find_pareto_optimal_outcomes(self)