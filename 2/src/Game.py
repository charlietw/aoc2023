class Game:
    def __init__(self, id):
        self.id = id
        self.rounds = []

    def add_round(self, round):
        self.rounds.append(round)

    def round_is_valid(self, round):
        red_max = 12
        green_max = 13
        blue_max = 14
        hands = round.split(",")
        for hand in hands:  # e.g. "3 blue, 4 red"
            components = hand.split()
            colour = components[1]  # e.g. "blue"
            count = int(components[0])  # e.g. 3
            if colour == "green" and count > green_max:
                return False
            elif colour == "red" and count > red_max:
                return False
            elif colour == "blue" and count > blue_max:
                return False
        return True

    def game_is_valid(self):
        for round in self.rounds:
            if self.round_is_valid(round) == False:
                return False
        return True
