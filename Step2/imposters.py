def main():
   # Adjacency matrix with the relations of the players
   graph = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]]

   players = set(range(10))
   suspects = set([1, 4, 5])

   for i in suspects:
        neighbours = set()
        for j in range(len(graph)):
            if graph[i][j]:
                neighbours.add(j)
                #saw the neighbours of the suspect
        print(f"Suspects if player {i} is an impostor: {players - neighbours - suspects}")
        #thos who are not the neighbourg of the suspect are suspects
if __name__ == "__main__":
    main()
