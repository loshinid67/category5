import heapq

graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 2, 'D': 5},
    'B': {'D': 1},
    'C': {'G': 5},
    'D': {'G': 3},
    'G': {}
}

h = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'G': 0
}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        print("Visiting:", node)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", g)
            return

        visited.add(node)

        for child, cost in graph[node].items():
            if child not in visited:
                new_g = g + cost
                new_f = new_g + h[child]

                heapq.heappush(
                    pq, (new_f, new_g, child, path + [child])
                )

    print("Goal Not Found")

astar('S', 'G')
