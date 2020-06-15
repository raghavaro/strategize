import plotly.express as px

def plot_normal_form_game(game):
    utilities = game.analyze()
    # assuming utilities array has shape 2,2,4
    utilities = utilities.reshape(4,4).transpose()
    print(utilities)

    fig = px.scatter(x=utilities[1], y=utilities[2], size=[3,3,3,3], color=utilities[3])
    print('X: Player 1 Utility, Y: Player 2 Utility')
    print('color: 0 is pareto dominated, 1 is pareto efficient')
    fig.show()