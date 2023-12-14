from src.Game import Game

FILENAME = "input.txt"

def get_id(input):
    words = input.split()
    id = words[1][:-1]
    return int(id)


def get_rounds(input):
    sections = input.split(":")
    rounds = sections[1].split(";")
    formatted_rounds = []
    for section in rounds:
        formatted_rounds.append(section.strip())
    return formatted_rounds

def main():
    result = 0
    with open(FILENAME) as file:
        for f in file:
            id = get_id(f)
            rounds = get_rounds(f)
            game = Game(id)
            for round in rounds:
                game.add_round(round)
            if game.game_is_valid():
                print(f"Game valid! Adding ID {game.id}")
                result += game.id
    print(result)


if __name__ == '__main__':
    main()