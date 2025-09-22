def dls(graph, node, goal, limit):
    if node == goal:
        return True
    if limit <= 0:
        return False
    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, limit-1):
            return True
    return False

# --- User Input ---
n = int(input("Enter number of nodes: "))
graph = {}

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated, leave blank if none): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

found = dls(graph, start, goal, limit)
print("Goal found?", found)
