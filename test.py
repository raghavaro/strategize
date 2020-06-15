import numpy as np
from src.strategize.game import Game

def prisoners_dilemma():
    player_set = np.array(['Alice', 'Bob'])
    action_set = np.array([['Cooperate', 'Defect'], ['Cooperate', 'Defect']])
    utility_set = np.array([[[2, 2], [0, 3]], [[3, 0], [1, 1]]])
    pd = Game(player_set, action_set, utility_set)
    return pd

def common_payoff():
    player_set = np.array(['Alice', 'Bob'])
    action_set = np.array([['Left', 'Right'], ['Left', 'Right']])
    utility_set = np.array([[[1, 1], [0, 0]], [[0, 0], [1, 1]]])
    cp = Game(player_set, action_set, utility_set)
    return cp

def zero_sum():
    player_set = np.array(['Alice', 'Bob'])
    action_set = np.array([['Heads', 'Tails'], ['Left', 'Right']])
    utility_set = np.array([[[1, -1], [-1, 1]], [[-1, 1], [1, -1]]])
    zs = Game(player_set, action_set, utility_set)
    return zs


game = prisoners_dilemma()
print(game)
game.plot()