import numpy as np    
    

def find_highest_reward_strategies(game):
    # Assuming 2p game with 2 choices each 
    num_rows = 4
    num_columns = 2
    # change shape from 2,2,2 to 4,2 
    utilities_row = np.reshape(game.u, (num_rows, num_columns))
    numbers = np.vstack(np.arange(num_rows))
    utilities_row = np.concatenate((numbers, utilities_row), axis=1)
    print('\n\n')
    print(utilities_row)
    print('\n\n')
    p1_indices = [0]
    p2_indices = [0]
    dominant_s1 = utilities_row[0][1]
    dominant_s2 = utilities_row[0][2]
    for s in utilities_row:
        if s[0] == 0:
            continue
        
        if s[1] > dominant_s1:
            dominant_s1 = s[1]
            p1_indices = [s[0]]
        elif s[1] == dominant_s1:
            p1_indices.append(s[0])
        
        if s[2] > dominant_s2:
            dominant_s2 = s[2]
            p2_indices = [s[0]]
        elif s[2] == dominant_s2:
            p2_indices.append(s[0])
    
    print(p1_indices)
    print(p2_indices)


def find_dominant_strategies(game):
    # Assuming 2p game with 2 choices each 
    pass