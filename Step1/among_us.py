import random
from player import Player
from tree import AVLTree

def game(turn, database):
    #Play 9 times and then go for the final for the 10th game
    if len(database.inorder_traverse()) > 10:
        print(f"\nGame number {turn+1}\n")
        lobbies = database.inorder_traverse()
        if turn < 3:
            #for 3 turns
            random.shuffle(lobbies)
        for lobby in range(0, len(lobbies), 10):
            win = random.randint(1,3) #1/3 to win
            print(f"Lobby {(lobby//10)+1}")
            imp1 = random.randint(0, 9)
            imp2 = random.randint(0, 9)
            #take 2 imposters
            while imp2 == imp1:
                imp2 = random.randint(0,9)
            for player in range(lobby, lobby+10):
                if (player - lobby == imp1) or (player - lobby == imp2):
                    #made the means of his 3 scores with the def score
                    lobbies[player].update_score(int(score(lobbies[player], win, True)/3))
                    print(f"Impostor {lobbies[player].name} has a score of {lobbies[player].score}")
                else:
                    lobbies[player].update_score(int(score(lobbies[player], win)/3))
                    print(f"Player {lobbies[player].name} has a score of {lobbies[player].score}")
        newDatabase = AVLTree()
        #new database without the 10 worsts
        [newDatabase.insert(player) for player in database.inorder_traverse()]    
        if turn >= 3:
            #after the 3rd turn, go for the next party
            [newDatabase.delete(newDatabase.get_min()) for _ in range(10)]
        return game(turn+1, newDatabase)
    final(database)

def final(database):
    print("\nThe final !\n")
    #the same but for the last game
    finalists = database.inorder_traverse()
    for player in finalists:
        player.reset_score()

    for game in range(5):
        print(f"\nGame number {game+1}\n")
        imp1 = random.randint(0, 9)
        imp2 = random.randint(0, 9)
        while imp2 == imp1:
            imp2 = random.randint(0, 9)

        win = random.randint(1,3) #1/3 to win
    
        for player in range(0, len(finalists)):
            if (player == imp1) or (player == imp2):
                finalists[player].update_score(int(score(finalists[player], win, True)))
                print(f"The finalist, impostor {finalists[player].name} has a score of {finalists[player].score}")
            else:
                finalists[player].update_score(int(score(finalists[player], win)/3))
                print(f"The finalist, player {finalists[player].name} has a score of {finalists[player].score}")

    newDatabase = AVLTree()
    [newDatabase.insert(player) for player in database.inorder_traverse()]
    print("\nPodium :")
    for i in range(10):
        #print the podium from the worst to the best
        print(f"{10-i} : Player {newDatabase.get_min().name} - {newDatabase.get_min().score} points")
        newDatabase.delete(newDatabase.get_min())
 
def score(player, win, impostor=False):
    score = 0
    if impostor:
        #if he is an imposter
        score += 10 if win == True else 0
        #if he wins
        murder = random.randint(0, 4)
        #how many murders he did
        for i in range(murder): #if undiscover or not
            score += 3 if random.randint(0, 4) == 1 else 1
    else :
        score += 5 if win == False else 0
        #if he made his tasks
        score += 1 if random.randint(1, 2) == 1 else 0
        #how many murder he discoved
        score += 3 * random.randint(0, 2)
    return score

if __name__ == "__main__":
    database = AVLTree()
    [database.insert(Player(i, 0)) for i in range(100)] 
    #create the database
    game(0, database)
