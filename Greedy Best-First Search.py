import heapq

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

h = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 4,
    'G': 0
}

def greedy_bfs(start, goal):
    pq = [(h[start], start)]
    visited = set()

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal Found!")
            return

        for child in graph[node]:
            if child not in visited:
                heapq.heappush(pq, (h[child], child))

    print("\nGoal Not Found!")

greedy_bfs('S', 'G')
