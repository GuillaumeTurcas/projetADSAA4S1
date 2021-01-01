class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.left = None
        self.right = None

    def update_score(self, newscore):
        self.score += newscore

    def reset_score(self):
        self.score = 0
