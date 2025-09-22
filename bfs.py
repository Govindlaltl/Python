from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            for i in (graph[node]):
                if i not in visited:
                    queue.append(i)
graph={}
num=int(input("Enter the number of nodes: "))
for j in range(num):
    node=input(f"Enter the node {j+1}:")
    neighbour=input(f"Enter the adjacent neighbours of {node} sepearted by spaces:").split()
    graph[node]=neighbour
start=input("Enter the starting node:")
print("BFS Traversal: ")
bfs(graph,start)

