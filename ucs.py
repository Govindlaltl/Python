import heapq
def ucs(graph,start,goal):
    visited=set()
    queue=[(0,start)]
    while queue:
        cost,node=heapq.heappop(queue)
        if node == goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbour,weight in graph.get(node,[]):
                heapq.heappush(queue,(cost+weight,neighbour))
    return-1
graph={}
num=int(input("Enter the number of nodes:"))
for i in range(num):
    node=input(f"Enter the node {i+1}: ")
    graph[node]=[]
    neigh=int(input(f"Enter the number of neighbouring nodes for{node}: " ))
    for j in range(neigh):
        neighbours,weights=input(f"Enter the neighbouring node and its wieght separated by spaces:").split()
        graph[node].append((neighbours,int(weights)))
Start=input("Enter the starting node:")
Goal=input("Enter the goal node:")  
print("UCS Traversal: ")
cost=ucs(graph,Start,Goal)
if cost!=-1:
    print(f"Cost from {Start} to {Goal} is {cost}")     
else:
    print(f"There is no path from {Start} to {Goal}")