import numpy as np

def find_pareto_optimal_outcomes(game):
    # Assuming 2p game with 2 choices each 
    num_rows = 4
    num_columns = 2
    # change shape from 2,2,2 to 4,2 
    utilities_row = np.reshape(game.u, (num_rows, num_columns))
    # add index to each utility
    numbers = np.vstack(np.arange(num_rows))
    utilities_row = np.concatenate((numbers, utilities_row), axis=1)
    
    # sort by player 1's utilities
    sorted_utilities_row = utilities_row[np.argsort(utilities_row[:,1])]
    
    dominated_indices = []

    for i in range(0, num_rows-1):
        original_index, p1_utility, p2_utility = sorted_utilities_row[i]
        for j in range(i+1, num_rows):
            if (sorted_utilities_row[j][2] >= p2_utility
                and sorted_utilities_row[j][1] > p1_utility)\
                or (sorted_utilities_row[j][2] > p2_utility
                and sorted_utilities_row[j][1] >= p1_utility):
                dominated_indices.append(original_index)
                break
    
    # create an array for pareto efficiency that stores 1 for pareto efficient outcomes and 0 for pareto dominated outcomes
    pareto_efficiency_array = np.vstack(np.array([0 if x in dominated_indices else 1 for x in np.arange(num_rows)]))
    utilities = np.concatenate((utilities_row, pareto_efficiency_array), axis=1).reshape(2,2,4)

    return utilities