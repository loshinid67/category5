graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 3},
    'E': {},
    'F': {'G': 1},
    'G': {}
}

h = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 3,
    'E': 5,
    'F': 1,
    'G': 0
}

def ida_star(start, goal):
    bound = h[start]
    path = [start]

    def search(node, g, bound):
        f = g + h[node]

        if f > bound:
            return f

        if node == goal:
            return True

        minimum = float('inf')

        for child, cost in graph[node].items():
            if child not in path:
                path.append(child)

                result = search(child, g + cost, bound)

                if result == True:
                    return True

                if result < minimum:
                    minimum = result

                path.pop()

        return minimum

    while True:
        result = search(start, 0, bound)

        if result == True:
            print("Path:", " -> ".join(path))
            print("Goal Found!")
            return

        if result == float('inf'):
            print("Goal Not Found!")
            return

        bound = result

ida_star('A', 'G')
