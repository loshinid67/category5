graph = {
    'A': [[('B', 1), ('C', 1)]],
    'B': [[('D', 1)], [('E', 1)]],
    'C': [[('F', 1), ('G', 1)]],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

h = {
    'A': 10,
    'B': 4,
    'C': 5,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0
}

def ao_star(node):
    if not graph[node]:
        return h[node]

    costs = []

    for option in graph[node]:
        cost = 0

        for child, edge_cost in option:
            cost += edge_cost + ao_star(child)

        costs.append(cost)

    h[node] = min(costs)
    return h[node]

ao_star('A')

print("Minimum Cost:", h['A'])
print("Updated Heuristic Values:")

for node in h:
    print(node, ":", h[node])
