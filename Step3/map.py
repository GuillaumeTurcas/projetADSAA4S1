import copy

def floyd_wharshall(solution_path, graph): 
    dist = copy.deepcopy(graph)
    for k in range(14): 
        for i in range(14): 
            for j in range(14): 
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 
    save_solution(solution_path, dist)
    #Floyd Wharshall algorithm

def save_solution(solution_path, dist):
    temp = copy.deepcopy(dist)
    for i in range(len(temp)):
        for j in range(len(temp)):
            if i != j:
                temp[i][j] = "INF" if temp[i][j] == float('inf') else temp[i][j]
            else:
                temp[i][j] = 0
    with open(solution_path, "w") as output:
        output.write(f"Rooms\t{[i+1 for i in range(14)]}\n\n")
        for i in range(len(temp)):
            output.write(f"{i+1}\t\t{temp[i]}\n")
            #print the solution in a .txt file

def solution(map_path, solution_path):
    map_file = open(map_path)
    graph = []
    for i in range(14):
        line = []
        for j in range(14):
            if i == j:
                line.append(0)
            else:
                line.append(float('inf'))
        graph.append(line) #creat a void map

    lines = map_file.readlines()

    for line in lines :
        i = line.rstrip()
        if i != '':
            line = i.replace(' ', '')
            graph[int(ord(line[0])-65)][int(ord(line[1])-65)] = int(line[2:])
            graph[int(ord(line[1])-65)][int(ord(line[0])-65)] = int(line[2:])
            #add the map.txt information in a matrix
            #because we use letter, we had to make the ord() to convert to a number

    floyd_wharshall(solution_path, graph) 

    print(f"Le fichier {solution_path} a été modifié !")

def main():
    solution("crewmatemap.txt", "solutioncrew.txt")
    solution("impostermap.txt", "solutionimpos.txt")

if __name__ == "__main__":
    main()
