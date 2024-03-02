graph = {
    'A' : ['B','C'],
    'B' : ['F','E'],
    'C' : ['E','D'],
    'D' : ['E'],
    'E' : ['G'],
    'F' : ['G'],
    'G' : []
}

heuristic = {
    'A' : 14,
    'B' : 12,
    'C' : 11,
    'D' : 6,
    'E' : 4,
    'F' : 11,
    'G' : 0
}

visited = []
queue = []

def Astar(visited,graph,heuristic,node):
    visited.append(node)
    queue.append(node)
    final = []
    while queue:
        m = queue.pop(0)
        final.append(m)
        print(m, end = " ")
        dict1 = {}
        mini = 100000
        for n in graph[m]:
            if n not in visited:
                print("\nEnter the Cost from ",m," to ",n)
                x = int(input("\nEnter : "))
                sum1 = x + heuristic[n]
                if(mini > sum1):
                    mini = sum1
                    dict1[n] = sum1
                
        if dict1:
            value = min(dict1, key=dict1.get)
            visited.append(value)
            queue.append(value)
            

    print(final)
Astar(visited,graph,heuristic,'A')

OUTPUT:
A 
Enter the Cost from  A  to  B

Enter : 4

Enter the Cost from  A  to  C

Enter : 3
C 
Enter the Cost from  C  to  E

Enter : 10

Enter the Cost from  C  to  D

Enter : 7
D 
Enter the Cost from  D  to  E

Enter : 2
E 
Enter the Cost from  E  to  G

Enter : 5

['A', 'C', 'D', 'E', 'G']
