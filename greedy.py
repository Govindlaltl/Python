import heapq
def greedy_best_first_search(graph, start, goal, heuristic):
    queue = [(heuristic[start], start)]
    visited = set()
    while queue:
        h, node = heapq.heappop(queue)
        print("Visiting:", node)        
        if node == goal:
            return True        
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor))
    return False
# --- User Input ---
n = int(input("Enter number of nodes: "))
graph = {}
heuristic = {}
for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated, leave blank if none): ").split()
    graph[node] = neighbors
    heuristic[node] = int(input(f"Enter heuristic value for {node} (estimate distance to goal): "))
start = input("Enter start node: ")
goal = input("Enter goal node: ")
found = greedy_best_first_search(graph, start, goal, heuristic)
print("Goal found?", found)
