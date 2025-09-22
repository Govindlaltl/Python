def dfs(graph,start):
    visited=set()
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            for i in reversed(graph[node]):
                if i not in visited:
                    stack.append(i)
graph={}
num=int(input("Enter the number of nodes:  "))
for i in range(num):
    node=input(f"Enter the node {i+1}: ")
    neighbour=input(f"Enter the adjacent neighbours of {node} separated by space: ").split()
    graph[node]=neighbour
start=input("Enter the starting node: ")
print("DFS Traversal: ")
dfs(graph,start)