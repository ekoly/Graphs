from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):

    child_to_parents = defaultdict(lambda: set())

    for parent, child in ancestors:
        child_to_parents[child].add(parent)

    if starting_node not in child_to_parents:
        return -1

    frontier = list(child_to_parents[starting_node])
    while True:
        new_frontier = []
        for node in frontier:
            new_frontier.extend(list(child_to_parents[node]))
        if not new_frontier:
            return frontier[-1]
        frontier = new_frontier
