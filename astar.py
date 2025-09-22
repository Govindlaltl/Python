import heapq
def astar(graph,start,goal,h):
    visited=()
    queue=[(h[start],0,start)]
    while queue:
        node,total,cost=heapq.heappop(queue)
        if node==goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbour,weight in graph(node):
                new_cost=cost+weight
                new_total=new_cost+h[neighbour]
                heapq.heappush(queue,(new_total,new_cost,neighbour))
    return -1
graph={}
h={}
num=int(input("Enter the number of nodes:"))
for i in range(num):
    node=input(f"Enter the ndoe {i+1}:")
    graph[node]=[]
    neigh=int(input(f"Enter the number of neighbouring nodes for {node}:"))
    for j in range(neigh):
        neighbours,weights=input(f"Enter the neighbouring node and its weight separated by spaces:").split()
        graph[node].append((neighbours,int(weights)))
    heauristic=int(input(f"Enter the heuristic value for {node}:"))
    h[node]=heauristic
Start=input("Enter the starting node:")
Goal=input("Enter the goal node:")
print("A* Traversal:")
cost=astar(graph,Start,Goal,h)
if cost!=-1:
    print(f"Cost from {Start} to {Goal} is {cost}")
else:
    print(f"There is no path from {Start} to {Goal}")