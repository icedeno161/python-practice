class Player:
    def __init__(self, name):
        self.name = name
        self.attempts = 0

    def guess(self):
        value = input(f"{self.name}, enter a guess: ")
        self.attempts += 1
        return int(value)

player = Player("Alex")
number = player.guess()
