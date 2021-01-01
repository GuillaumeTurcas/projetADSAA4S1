from collections import defaultdict

crewgraph = {1: set([2, 3, 4]),
         2: set([1, 3, 4, 5, 7]),
         3: set([1, 2, 4, 6, 8]),
         4: set([1, 2, 3]),
         5: set([2, 7]),
         6: set([3, 8]),
         7: set([2, 5, 8, 9, 10]),
         8: set([3, 6, 7, 9, 13, 14]),
         9: set([7, 8]),
         10: set([7, 11, 12, 13]),
         11: set([10, 12, 13]),
         12: set([10, 11, 13]),
         13: set([8, 10, 11, 12, 14]),
         14: set([8, 13])}
         #create the crew graph with a dictionnary for our hamilton recursive fonction
         
def hamilton_recursive(graph, point, path=[]):
    #hamilton algorithm to find the best path
    if point not in path:
        path.append(point)

        if len(path) == len(graph):
            return path

        for point_next in graph[point]:
            path_copy = [i for i in path]
            candidate = hamilton_recursive(graph, point_next, path_copy)
            if candidate:
                return candidate

def main():
    #we have to start from Medbay, because if not it doesnt works
    print(f"Hamiltonian path starting from Medbay: {hamilton_recursive(crewgraph, 5)}")

if __name__ == "__main__":
    main()
