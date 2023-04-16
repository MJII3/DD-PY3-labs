from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    a =graph.number_of_nodes(-1)
    min_cost = nx.dijkstra_path_length(graph, 0, a)
    return min_cost

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = nx.DiGraph()
    stairway_graph.add_weighted_edges_from([
        (0, 1, 5),
        (0, 2, 11),
        (1, 2, 11),
        (1, 3, 43),
        (2, 3, 43),
        (2, 4, 2),
        (3, 4, 2)])
    print(stairway_path(stairway_graph))  # 72
