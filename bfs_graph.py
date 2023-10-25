# bfs_graph.py

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue.extend(self.graph[node])

        return result

# Example usage:
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # Perform BFS starting from vertex 2
    bfs_result = g.bfs(2)

    print("Breadth-First Search Result:", bfs_result)
