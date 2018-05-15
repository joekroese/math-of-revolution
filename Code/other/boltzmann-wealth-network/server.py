from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import NetworkModule

from model import MoneyModel


def network_portrayal(G):
    # The model ensures there is 0 or 1 agent per node

    portrayal = dict()
    portrayal['nodes'] = [{'id': n_id,
                           'agent_id': None if not n['agent'] else n['agent'][0].unique_id,
                           'size': 3 if n['agent'] else 1,
                           'color': '#CC0000' if not n['agent'] or n['agent'][0].wealth == 0 else '#007959',
                           'label': None if not n['agent'] else 'Agent:{} Wealth:{}'.format(n['agent'][0].unique_id,
                                                                                            n['agent'][0].wealth),
                           }
                          for n_id, n in G.nodes(data=True)]

    portrayal['edges'] = [{'id': i,
                           'source': source,
                           'target': target,
                           'color': '#000000',
                           }
                          for i, (source, target, _) in enumerate(G.edges(data=True))]

    return portrayal


grid = NetworkModule(network_portrayal, 500, 500, library='sigma')
# chart = ChartModule([
#     {"Label": "Gini", "Color": "Black"}],
#     data_collector_name='datacollector'
# )

model_params = {
    "num_agents": UserSettableParameter('slider', "Number of agents", 7, 2, 50, 1,
                                        description="Choose how many agents to include in the model"),
    # "num_nodes": UserSettableParameter('slider', "Number of nodes", 10, 3, 12, 1,
    #                                    description="Choose how many nodes to include in the model, with at "
    #                                                "least the same number of agents")
}

server = ModularServer(MoneyModel, [grid], "Money Model", model_params)
server.port = 8521
